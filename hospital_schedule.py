import streamlit as st
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Time, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# ------------------- Database Setup -------------------
Base = declarative_base()

class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    recurring = Column(Boolean, default=False)
    recurrence_interval = Column(Integer, nullable=True)

engine = create_engine('sqlite:///hospital_schedule.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# ------------------- Streamlit App -------------------
st.set_page_config(page_title="Hospital Scheduling System", layout="wide")
st.title("🏥 Hospital Scheduling System")

# ------------------- Insert Header Image -------------------
# TODO: Replace 'path_to_header_image.jpg' with your image file path or URL
# st.image("path_to_header_image.jpg", use_column_width=True)

# ------------------- Navigation Sidebar -------------------
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Add Schedule", "View Schedule", "Emergency"])

# ------------------- Function to Populate Recurring Schedules -------------------
def populate_recurring_schedules():
    today = datetime.today().date()
    schedules = session.query(Schedule).filter(Schedule.recurring == True).all()
    for schedule in schedules:
        next_date = schedule.date
        while next_date <= today:
            next_date += timedelta(days=schedule.recurrence_interval)
        if next_date == today:
            existing = session.query(Schedule).filter(
                Schedule.date == today,
                Schedule.time == schedule.time,
                Schedule.description == schedule.description
            ).first()
            if not existing:
                new_schedule = Schedule(
                    date=next_date,
                    time=schedule.time,
                    description=schedule.description,
                    type=schedule.type,
                    recurring=schedule.recurring,
                    recurrence_interval=schedule.recurrence_interval
                )
                session.add(new_schedule)
    session.commit()

# Populate recurring schedules at the start
populate_recurring_schedules()

# ------------------- Add Schedule Section -------------------
if options == "Add Schedule":
    st.header("📝 Add New Schedule")
    
    # ------------------- Insert Add Schedule Image -------------------
    # TODO: Replace 'path_to_add_schedule_image.jpg' with your image file path or URL
    # st.image("path_to_add_schedule_image.jpg", use_column_width=True)
    
    with st.form("schedule_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            date = st.date_input("📅 Date", datetime.today())
        with col2:
            time = st.time_input("🕒 Time", datetime.now().time())
        
        description = st.text_input("📝 Description")
        schedule_type = st.selectbox("📋 Type", [
            "Doctor Visit", "Nurse Checkup", "Physiotherapy",
            "Specialist Visit", "MRI/CT Test", "BP/Sugar Test",
            "Meal", "Patient Visit"
        ])
        recurring = st.checkbox("🔄 Recurring")
        
        if recurring:
            if schedule_type == "Specialist Visit":
                recurrence_interval = 2  # Every two days
                st.info("Specialist Visit is set to recur every 2 days.")
            elif schedule_type in ["MRI/CT Test"]:
                recurrence_interval = 30  # Every month
                st.info("MRI/CT Test is set to recur monthly.")
            elif schedule_type == "Physiotherapy":
                recurrence_interval = 1  # Daily
                st.info("Physiotherapy is set to recur daily.")
            else:
                recurrence_interval = st.number_input("🔢 Recurrence Interval (days)", min_value=1, value=1)
        else:
            recurrence_interval = None
        
        submit = st.form_submit_button("➕ Add Schedule")
    
    if submit:
        new_schedule = Schedule(
            date=date,
            time=time,
            description=description,
            type=schedule_type,
            recurring=recurring,
            recurrence_interval=recurrence_interval
        )
        session.add(new_schedule)
        session.commit()
        st.success("✅ Schedule added successfully!")

# ------------------- View Schedule Section -------------------
elif options == "View Schedule":
    st.header("📅 View Daily Schedule")
    
    # ------------------- Insert View Schedule Image -------------------
    # TODO: Replace 'path_to_view_schedule_image.jpg' with your image file path or URL
    # st.image("path_to_view_schedule_image.jpg", use_column_width=True)
    
    selected_date = st.date_input("Select Date", datetime.today())
    
    # Query schedules for the selected date
    schedules = session.query(Schedule).filter(Schedule.date == selected_date).all()
    
    if schedules:
        data = [{
            "ID": schedule.id,
            "Time": schedule.time.strftime("%H:%M"),
            "Description": schedule.description,
            "Type": schedule.type
        } for schedule in schedules]
        
        df = pd.DataFrame(data)
        df = df.sort_values(by="Time")
        df = df.reset_index(drop=True)
        
        st.subheader("🗓️ Scheduled Activities")
        st.table(df[['Time', 'Description', 'Type']])
        
        st.subheader("🗑️ Delete Schedule")
        for idx, row in df.iterrows():
            col1, col2 = st.columns([4,1])
            with col1:
                st.write(f"**{row['Time']}** - {row['Description']} ({row['Type']})")
            with col2:
                if st.button("🗑️ Delete", key=row['ID']):
                    session.delete(session.query(Schedule).filter(Schedule.id == row['ID']).first())
                    session.commit()
                    st.success("✅ Schedule deleted successfully!")
                    st.experimental_rerun()  # Refresh the page to update the schedule list
    else:
        st.info("ℹ️ No schedules for this date.")

# ------------------- Emergency Section -------------------
elif options == "Emergency":
    st.header("🚨 Medical Emergency")
    
    # ------------------- Insert Emergency Image -------------------
    # TODO: Replace 'path_to_emergency_image.jpg' with your image file path or URL
    # st.image("path_to_emergency_image.jpg", use_column_width=True)
    
    with st.form("emergency_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            date = st.date_input("📅 Date", datetime.today())
        with col2:
            time = st.time_input("🕒 Time", datetime.now().time())
        
        description = st.text_area("📝 Description")
        submit = st.form_submit_button("🚑 Log Emergency")
    
    if submit:
        emergency = Schedule(
            date=date,
            time=time,
            description=description,
            type="Emergency",
            recurring=False
        )
        session.add(emergency)
        session.commit()
        st.success("✅ Emergency logged successfully!")
    
    st.subheader("📋 Today's Emergencies")
    today = datetime.today().date()
    emergencies = session.query(Schedule).filter(
        Schedule.date == today,
        Schedule.type == "Emergency"
    ).all()
    
    if emergencies:
        data = [{
            "ID": e.id,
            "Time": e.time.strftime("%H:%M"),
            "Description": e.description
        } for e in emergencies]
        
        df = pd.DataFrame(data)
        df = df.sort_values(by="Time")
        df = df.reset_index(drop=True)
        
        st.table(df[['Time', 'Description']])
        
        st.subheader("🗑️ Delete Emergency")
        for idx, row in df.iterrows():
            col1, col2 = st.columns([4,1])
            with col1:
                st.write(f"**{row['Time']}** - {row['Description']}")
            with col2:
                if st.button("🗑️ Delete", key=row['ID']):
                    session.delete(session.query(Schedule).filter(Schedule.id == row['ID']).first())
                    session.commit()
                    st.success("✅ Emergency deleted successfully!")
                    st.experimental_rerun()  # Refresh the page to update the emergencies list
    else:
        st.info("ℹ️ No emergencies today.")

# ------------------- Footer with Images/Icons -------------------
# TODO: Add footer images or icons if needed
# st.image("path_to_footer_image.jpg", use_column_width=True)
