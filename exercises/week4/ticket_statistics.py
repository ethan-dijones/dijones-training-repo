"""
Exercise 4.3: Structured Data - Ticket Statistics Generator

Objective: Work with structured data (CSV files)

This module demonstrates:
- Reading CSV data
- Parsing and organizing structured data
- Calculating statistics and aggregations
- Generating formatted reports
- Saving results as HTML
- Creating text-based visualizations
"""

import csv
from collections import defaultdict


def load_csv_data(filename):
    """
    Load ticket data from CSV file.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of dictionaries representing tickets
    """
    tickets = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tickets.append(row)
        print(f"Successfully loaded {len(tickets)} tickets from '{filename}'")
        return tickets
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as error:
        print(f"Error reading CSV: {error}")
        return []


def calculate_status_counts(tickets):
    """
    Calculate total open and closed tickets.
    
    Args:
        tickets (list): List of ticket dictionaries
        
    Returns:
        dict: Dictionary with status counts
    """
    status_counts = defaultdict(int)
    for ticket in tickets:
        status = ticket['status']
        status_counts[status] += 1
    return dict(status_counts)


def calculate_tickets_per_person(tickets):
    """
    Calculate number of tickets assigned to each person.
    
    Args:
        tickets (list): List of ticket dictionaries
        
    Returns:
        dict: Dictionary with person names and ticket counts
    """
    person_counts = defaultdict(int)
    for ticket in tickets:
        assigned_to = ticket['assigned_to']
        person_counts[assigned_to] += 1
    return dict(sorted(person_counts.items()))


def calculate_priority_stats(tickets):
    """
    Calculate statistics grouped by priority level.
    
    Args:
        tickets (list): List of ticket dictionaries
        
    Returns:
        dict: Dictionary with priority statistics
    """
    priority_stats = defaultdict(lambda: {'count': 0, 'open': 0, 'closed': 0})
    
    for ticket in tickets:
        priority = ticket['priority']
        status = ticket['status']
        
        priority_stats[priority]['count'] += 1
        if status == 'open':
            priority_stats[priority]['open'] += 1
        else:
            priority_stats[priority]['closed'] += 1
    
    return dict(sorted(priority_stats.items()))


def create_text_chart(data, max_width=40):
    """
    Create a simple text-based bar chart.
    
    Args:
        data (dict): Dictionary with labels and values
        max_width (int): Maximum width of the chart in characters
        
    Returns:
        str: Formatted chart as string
    """
    if not data:
        return "No data to display"
    
    max_value = max(data.values()) if data.values() else 1
    chart = "TEXT BAR CHART\n" + "=" * 50 + "\n\n"
    
    for label, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
        bar_length = int((value / max_value) * max_width) if max_value > 0 else 0
        bar = "█" * bar_length
        chart += f"{label:15} : {bar:40} {value}\n"
    
    chart += "\n" + "=" * 50 + "\n"
    return chart


def generate_report(tickets):
    """
    Generate a comprehensive statistics report.
    
    Args:
        tickets (list): List of ticket dictionaries
        
    Returns:
        str: Formatted report
    """
    if not tickets:
        return "No ticket data available"
    
    total_tickets = len(tickets)
    status_counts = calculate_status_counts(tickets)
    person_counts = calculate_tickets_per_person(tickets)
    priority_stats = calculate_priority_stats(tickets)
    
    report = "=" * 70 + "\n"
    report += "TICKET STATISTICS REPORT\n"
    report += "=" * 70 + "\n\n"
    
    # Overall statistics
    report += "OVERALL STATISTICS:\n"
    report += "-" * 70 + "\n"
    report += f"Total Tickets: {total_tickets}\n"
    for status, count in sorted(status_counts.items()):
        percentage = (count / total_tickets) * 100
        report += f"  {status.capitalize():10}: {count:3} ({percentage:5.1f}%)\n"
    
    report += "\n"
    
    # Tickets per person
    report += "TICKETS PER ASSIGNED PERSON:\n"
    report += "-" * 70 + "\n"
    for person, count in sorted(person_counts.items(), key=lambda x: x[1], reverse=True):
        report += f"  {person:15}: {count:3} tickets\n"
    
    report += "\n"
    
    # Priority breakdown
    report += "TICKETS BY PRIORITY:\n"
    report += "-" * 70 + "\n"
    for priority, stats in sorted(priority_stats.items()):
        report += f"  {priority.capitalize():10}: {stats['count']:3} total "
        report += f"({stats['open']} open, {stats['closed']} closed)\n"
    
    report += "\n" + "=" * 70 + "\n"
    
    return report


def save_as_html(tickets, filename):
    """
    Save ticket data as an HTML table.
    
    Args:
        tickets (list): List of ticket dictionaries
        filename (str): Output HTML filename
    """
    try:
        html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Ticket Statistics</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th {
            background-color: #667eea;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }
        td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f0f0f0;
        }
        .status-open {
            color: #4caf50;
            font-weight: bold;
        }
        .status-closed {
            color: #999;
        }
        .priority-high {
            color: #f44336;
            font-weight: bold;
        }
        .priority-medium {
            color: #ff9800;
        }
        .priority-low {
            color: #4caf50;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ticket Statistics</h1>
        <table>
            <thead>
                <tr>
                    <th>Ticket ID</th>
                    <th>Status</th>
                    <th>Priority</th>
                    <th>Assigned To</th>
                    <th>Created Date</th>
                </tr>
            </thead>
            <tbody>
"""
        
        # Add table rows
        for ticket in tickets:
            status_class = f"status-{ticket['status']}"
            priority_class = f"priority-{ticket['priority']}"
            
            html_content += f"""                <tr>
                    <td>{ticket['ticket_id']}</td>
                    <td class="{status_class}">{ticket['status'].capitalize()}</td>
                    <td class="{priority_class}">{ticket['priority'].capitalize()}</td>
                    <td>{ticket['assigned_to']}</td>
                    <td>{ticket['created_date']}</td>
                </tr>
"""
        
        html_content += """            </tbody>
        </table>
    </div>
</body>
</html>
"""
        
        with open(filename, 'w') as f:
            f.write(html_content)
        print(f"HTML report saved to '{filename}'")
    except IOError as error:
        print(f"Error writing HTML file: {error}")


if __name__ == "__main__":
    csv_file = "tickets.csv"
    
    # Load data
    print("Loading ticket data...\n")
    tickets = load_csv_data(csv_file)
    
    if tickets:
        # Calculate statistics
        total_tickets = len(tickets)
        status_counts = calculate_status_counts(tickets)
        person_counts = calculate_tickets_per_person(tickets)
        priority_stats = calculate_priority_stats(tickets)
        
        # Generate and display report
        report = generate_report(tickets)
        print(report)
        
        # Display text-based charts
        print("\nTICKETS ASSIGNED BY PERSON:\n")
        print(create_text_chart(person_counts))
        
        print("\nTICKETS BY STATUS:\n")
        print(create_text_chart(status_counts))
        
        # Save as HTML
        html_file = "ticket_statistics.html"
        save_as_html(tickets, html_file)
        
        # Save text report to file
        try:
            with open("ticket_statistics_report.txt", 'w') as f:
                f.write(report)
                f.write("\n\nTICKETS ASSIGNED BY PERSON:\n")
                f.write(create_text_chart(person_counts))
                f.write("\nTICKETS BY STATUS:\n")
                f.write(create_text_chart(status_counts))
            print(f"Text report saved to 'ticket_statistics_report.txt'")
        except IOError as error:
            print(f"Error writing report file: {error}")
    else:
        print("No data loaded. Please check the CSV file.")
