import random
import time

def generate_noisy_data(num_entries=50):
    """Simulates a stream of diverse, often noisy, log entries.
    Represents the 'noisy tech world' with various types of information.
    """
    data = []
    common_messages = [
        "INFO: User activity detected.",
        "DEBUG: Cache refreshed.",
        "WARNING: Low disk space on /tmp.",
        "INFO: Background task completed.",
        "DEBUG: Network check successful.",
        "INFO: Database connection established."
    ]
    critical_events = [
        "CRITICAL: Unauthorized access attempt detected from IP 192.168.1.100. User 'admin' failed login.",
        "ANOMALY: High CPU usage detected on server 'web-01'. Process 'data_miner' consuming 95%.",
        "SECURITY: Unusual outbound connection to unknown_host.com on port 443. Origin: internal_service_X."
    ]

    for i in range(num_entries):
        if random.random() < 0.1: # 10% chance for a critical event
            data.append(random.choice(critical_events))
        else:
            data.append(random.choice(common_messages))
        # Add some random "noise" that might look important but isn't the target
        if random.random() < 0.05:
            data.append(f"ADVERT: Buy our new product! {random.randint(1000, 9999)}")
        if random.random() < 0.03:
            data.append(f"SPAM: You've won a prize! Click here: {random.choice(['bit.ly/fake', 'tinyurl.com/scam'])}")

    random.shuffle(data) # Mix them up
    return data

def analyze_logs_for_insights(log_entries):
    """
    Simulates an 'introvert's approach' to data analysis:
    deep focus, attention to detail, and careful pattern recognition
    to find critical insights amidst noise.
    """
    print("Starting deep analysis of log entries...")
    insights = []
    potential_threats = []
    anomalies = []

    for i, entry in enumerate(log_entries):
        # Simulate deep thinking/processing time (conceptually, not literally slowing down)
        # time.sleep(0.01) # Uncomment to visually slow down processing

        # --- This is where the 'introvert's detailed focus' comes in ---
        # Carefully checking for specific keywords and patterns, ignoring superficial noise.
        if "CRITICAL: Unauthorized access" in entry:
            insights.append(f"[{i}] Found CRITICAL SECURITY ALERT: {entry}")
            potential_threats.append(entry)
        elif "ANOMALY: High CPU usage" in entry and "data_miner" in entry:
            insights.append(f"[{i}] Found SYSTEM ANOMALY (CPU): {entry}")
            anomalies.append(entry)
        elif "SECURITY: Unusual outbound connection" in entry:
            insights.append(f"[{i}] Found POTENTIAL OUTBOUND THREAT: {entry}")
            potential_threats.append(entry)
        # Explicitly ignoring known noise, demonstrating selective focus.
        elif "ADVERT:" in entry or "SPAM:" in entry:
            pass # These are filtered out as irrelevant noise
        # Other general INFO/DEBUG messages are also treated as background noise for this specific task.

    print("\nDeep analysis complete. Extracted insights:")
    if not insights:
        print("No specific insights found in this batch.")
    return insights, potential_threats, anomalies

if __name__ == "__main__":
    noisy_log_data = generate_noisy_data(num_entries=100)

    # An introvert's strength: meticulously sifting through information
    # to find the truly important details, rather than reacting to every piece of data.
    found_insights, threats, system_anomalies = analyze_logs_for_insights(noisy_log_data)

    print("\n--- Summary of Critical Findings ---")
    if found_insights:
        for insight in found_insights:
            print(f"- {insight}")
    else:
        print("No critical insights were identified.")

    print(f"\nTotal entries analyzed: {len(noisy_log_data)}")
    print(f"Critical security threats identified: {len(threats)}")
    print(f"System anomalies identified: {len(system_anomalies)}")
    print("\nThis demonstrates how focused, detailed analysis (akin to an introvert's approach) can uncover critical information in a 'noisy' data stream.")
