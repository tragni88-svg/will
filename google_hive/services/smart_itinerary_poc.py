
import re
from datetime import datetime, timedelta

# --- Simulated Raw Data (from Google APIs) ---

# A simplified email body from a Gmail API response
GMAIL_EMAIL_BODY = """
Your flight confirmation for United Airlines flight UA 456.
Departure: San Francisco (SFO) on 2026-02-15 at 10:00 AM PST.
Arrival: New York (JFK) on 2026-02-15 at 6:15 PM EST.
"""

# A simplified list of events from a Google Calendar API response
CALENDAR_EVENTS = [
    {
        "summary": "Project X Team Sync",
        "start": {"dateTime": "2026-02-15T19:00:00-05:00"}, # 7:00 PM EST
        "end": {"dateTime": "2026-02-15T20:00:00-05:00"},
        "location": "111 8th Ave, New York, NY 10011"
    },
    {
        "summary": "Dinner with Sarah",
        "start": {"dateTime": "2026-02-16T19:30:00-05:00"},
        "end": {"dateTime": "2026-02-16T21:00:00-05:00"},
        "location": "456 Carmine St, New York, NY 10014"
    }
]

# Simulated FanBasis Transaction Data
FANBASIS_TRANSACTIONS = [
    {
        "id": "FB-TX-998877",
        "merchant": "Madison Square Garden",
        "item": "Knicks vs Lakers - Courtside Seats",
        "amount": 4500.00,
        "timestamp": "2026-02-14T15:30:00-05:00",
        "metadata": {
            "event_date": "2026-02-15T20:30:00-05:00", # 8:30 PM EST
            "location": "4 Pennsylvania Plaza, New York, NY 10001"
        }
    }
]

# A simplified response from the Google Maps Distance Matrix API
# (Simulating a 45-minute travel time from JFK to the meeting location)
MAPS_TRAVEL_TIME_SECONDS = 2700

# --- Intelligence Engine: Proof-of-Concept ---

def parse_flight_from_email(email_body):
    """Uses regex to parse flight details from an email body."""
    print("[Engine] Parsing flight details from email...")
    flight_match = re.search(r"flight (UA \d+)", email_body)
    arrival_match = re.search(r"Arrival: .* \((\w+)\) on (.*) at (.*)", email_body)
    
    if flight_match and arrival_match:
        flight_number = flight_match.group(1)
        arrival_airport = arrival_match.group(1)
        arrival_date_str = arrival_match.group(2)
        arrival_time_str = arrival_match.group(3).strip('.')
        
        # Combine date and time and parse into a datetime object
        # Note: In a real app, we'd handle timezones robustly.
        arrival_datetime = datetime.strptime(f"{arrival_date_str} {arrival_time_str}", "%Y-%m-%d %I:%M %p EST")
        
        flight_event = {
            "type": "Flight",
            "flight_number": flight_number,
            "arrival_airport": arrival_airport,
            "arrival_time": arrival_datetime
        }
        print(f"[Engine] Found Flight Event: {flight_event['flight_number']}")
        return flight_event
    return None

def find_related_calendar_event(flight_event, calendar_events):
    """Finds a calendar event that occurs shortly after the flight lands."""
    print("\n[Engine] Searching for related calendar events...")
    for event in calendar_events:
        event_start_time = datetime.fromisoformat(event["start"]["dateTime"]).replace(tzinfo=None)
        
        # Check if the event is on the same day and after the flight lands
        time_diff = event_start_time - flight_event["arrival_time"]
        if 0 < time_diff.total_seconds() < 4 * 3600: # Within 4 hours after landing
            print(f"[Engine] Found related event: '{event['summary']}'")
            return event
    return None

def process_fanbasis_transactions(transactions):
    """Analyzes FanBasis transactions for actionable insights."""
    print("\n[Engine] Analyzing FanBasis transaction history...")
    insights = []
    for tx in transactions:
        print(f"[Engine] Found Purchase: {tx['item']} for ${tx['amount']}")
        
        # Check if purchase has event metadata
        if "metadata" in tx and "event_date" in tx["metadata"]:
            event_time = datetime.fromisoformat(tx["metadata"]["event_date"]).replace(tzinfo=None)
            
            insight = {
                "type": "FanBasis Event",
                "summary": tx['item'],
                "start": event_time,
                "location": tx['metadata']['location'],
                "cost": tx['amount']
            }
            insights.append(insight)
    return insights

def generate_proactive_notification(flight, meeting, travel_time_seconds, fanbasis_events=None):
    """Generates a human-readable, proactive notification."""
    print("\n[Engine] Generating proactive notification...")
    
    travel_delta = timedelta(seconds=travel_time_seconds)
    meeting_start_time = datetime.fromisoformat(meeting["start"]["dateTime"]).replace(tzinfo=None)
    required_departure_time = meeting_start_time - travel_delta
    
    notification = f"""\
    **Google Hive Alert**
    ---------------------
    Your flight {flight['flight_number']} is scheduled to land at {flight['arrival_time'].strftime('%#I:%M %p')}.
    You have a meeting, '{meeting['summary']}', at {meeting_start_time.strftime('%#I:%M %p')}.
    Based on current traffic, travel from {flight['arrival_airport']} to the meeting will take approximately {int(travel_delta.total_seconds() / 60)} minutes.
    
    **Recommendation:** You should plan to leave the airport by **{required_departure_time.strftime('%#I:%M %p')}**.
    """

    if fanbasis_events:
        notification += "\n    **FanBasis Integration**\n    ---------------------\n"
        for event in fanbasis_events:
            # Check for conflict
            if abs((event['start'] - meeting_start_time).total_seconds()) < 7200: # 2 hour buffer
                notification += f"    ⚠️  CONFLICT DETECTED: Your purchased event '{event['summary']}' starts at {event['start'].strftime('%#I:%M %p')}, close to your meeting time.\n"
            else:
                notification += f"    Note: You have tickets for '{event['summary']}' later at {event['start'].strftime('%#I:%M %p')}.\n"
                
    return notification

def main():
    """Main function to run the Smart Itinerary Proof-of-Concept."""
    print("===========================================")
    print("=== HIVE SMART ITINERARY PoC (SIMULATED) ===")
    print("===========================================")
    
    # 1. Ingest and parse data from Google services
    flight = parse_flight_from_email(GMAIL_EMAIL_BODY)
    
    if flight:
        # 2. Find relationships between events
        related_meeting = find_related_calendar_event(flight, CALENDAR_EVENTS)
        
        if related_meeting:
            # 3. Get contextual data (e.g., traffic)
            # (Using a simulated value here)
            travel_time = MAPS_TRAVEL_TIME_SECONDS
            
            # 4. Integrate FanBasis Data
            fanbasis_insights = process_fanbasis_transactions(FANBASIS_TRANSACTIONS)
            
            # 5. Generate the proactive insight
            notification = generate_proactive_notification(flight, related_meeting, travel_time, fanbasis_insights)
            
            print("\n--- FINAL NOTIFICATION ---")
            print(notification)
        else:
            print("\n[Engine] No relevant upcoming meetings found.")
    else:
        print("\n[Engine] No flight information found in the provided email.")

    print("\n===========================================")
    print("===         SIMULATION COMPLETE         ===")
    print("===========================================")

if __name__ == "__main__":
    main()
