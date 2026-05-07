# 1. Create realistic sample ticket data
sample_tickets = [
    {
        "id": "TKT001",
        "status": "open",
        "priority": "high",
        "description": "Finance team cannot log in after password reset",
        "created_date": "2026-05-01",
        "assigned_to": "Ava Patel",
        "category": "authentication"
    },
    {
        "id": "TKT002",
        "status": "in_progress",
        "priority": "medium",
        "description": "Printer on floor 3 is showing a paper jam error",
        "created_date": "2026-05-02",
        "assigned_to": "Marcus Lee",
        "category": "hardware"
    },
    {
        "id": "TKT003",
        "status": "resolved",
        "priority": "low",
        "description": "Request to install Zoom on a new laptop",
        "created_date": "2026-05-02",
        "assigned_to": "Nina Brooks",
        "category": "software"
    },
    {
        "id": "TKT004",
        "status": "open",
        "priority": "critical",
        "description": "Customer portal returns 500 error during checkout",
        "created_date": "2026-05-03",
        "assigned_to": "Owen Carter",
        "category": "production"
    },
    {
        "id": "TKT005",
        "status": "waiting_on_user",
        "priority": "medium",
        "description": "VPN disconnects every 15 minutes for remote employee",
        "created_date": "2026-05-03",
        "assigned_to": "Priya Shah",
        "category": "network"
    },
    {
        "id": "TKT006",
        "status": "resolved",
        "priority": "high",
        "description": "Shared mailbox permissions missing for support team",
        "created_date": "2026-05-04",
        "assigned_to": "Jordan Kim",
        "category": "email"
    },
    {
        "id": "TKT007",
        "status": "in_progress",
        "priority": "high",
        "description": "Payroll report export timing out for HR manager",
        "created_date": "2026-05-04",
        "assigned_to": "Sofia Nguyen",
        "category": "reporting"
    },
    {
        "id": "TKT008",
        "status": "closed",
        "priority": "low",
        "description": "Update email signature for new job title",
        "created_date": "2026-05-05",
        "assigned_to": "Liam Turner",
        "category": "account"
    },
    {
        "id": "TKT009",
        "status": "open",
        "priority": "medium",
        "description": "Meeting room tablet is offline and not syncing calendar",
        "created_date": "2026-05-06",
        "assigned_to": "Emma Davis",
        "category": "device"
    },
    {
        "id": "TKT010",
        "status": "in_progress",
        "priority": "critical",
        "description": "Security alert triggered by repeated failed admin logins",
        "created_date": "2026-05-06",
        "assigned_to": "Noah Wilson",
        "category": "security"
    }
]

# 2. Create a list of ticket IDs using a list comprehension
ticket_ids = [ticket["id"] for ticket in sample_tickets]

# 3. Create a dictionary representing a single sample ticket
sample_ticket = sample_tickets[0]

# 4. Function to print ticket information in readable format
def print_ticket(ticket):
    """Print ticket information in readable format."""
    print(f"ID: {ticket['id']}")
    print(f"Status: {ticket['status']}")
    print(f"Priority: {ticket['priority']}")
    print(f"Description: {ticket['description']}")
    print(f"Created Date: {ticket['created_date']}")
    print("-" * 40)

# 5. Function to filter tickets by status
def filter_tickets_by_status(tickets, status):
    """Filter tickets by status."""
    return [ticket for ticket in tickets if ticket['status'] == status]

# 6. Function to count tickets by priority level
def count_tickets_by_priority(tickets):
    """Count tickets by priority level."""
    priority_counts = {}
    for ticket in tickets:
        priority = ticket['priority']
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    return priority_counts

# 7. Function to calculate the average of a list of numbers
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): List of numeric values
        
    Returns:
        float: Average value, or 0 if list is empty
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 8. Create a dictionary with user information (name, email, role)
user_info = {
    "name": "John Smith",
    "email": "john.smith@company.com",
    "role": "Support Technician"
}

# 9. Function to check if a ticket ID is valid (5 digits)
def is_valid_ticket_id(ticket_id):
    """
    Check if a ticket ID is valid (format: TKTXXX where X is a digit).
    
    Args:
        ticket_id (str): Ticket ID to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if len(ticket_id) != 6:
        return False
    if not ticket_id.startswith("TKT"):
        return False
    return ticket_id[3:].isdigit()

# 10. Loop through a list of tickets and print open ones
def print_open_tickets(tickets):
    """
    Loop through tickets and print all open ones.
    
    Args:
        tickets (list): List of ticket dictionaries
    """
    print("\nOPEN TICKETS:")
    print("-" * 60)
    open_count = 0
    for ticket in tickets:
        if ticket['status'] == 'open':
            print(f"ID: {ticket['id']:<10} Priority: {ticket['priority']:<10} "
                  f"Assigned: {ticket['assigned_to']:<15} {ticket['description']}")
            open_count += 1
    print(f"\nTotal open tickets: {open_count}")
    print("-" * 60)

# 11. Function to read a text file and return its contents
def read_text_file(filename):
    """
    Read a text file and return its contents.
    
    Args:
        filename (str): Path to the file
        
    Returns:
        str: File contents, or empty string if file not found
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return ""

# 12. Function to write a list of items to a file, one per line
def write_list_to_file(filename, items):
    """
    Write a list of items to a file, one per line.
    
    Args:
        filename (str): Path to the file
        items (list): List of items to write
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w') as file:
            for item in items:
                file.write(str(item) + '\n')
        print(f"Successfully wrote {len(items)} items to {filename}")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

# 13. Read a CSV file and return data as list of dictionaries
def read_csv_file(filename):
    """
    Read a CSV file and return data as list of dictionaries.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of dictionaries (one per row), or empty list if error
    """
    import csv
    try:
        data = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        print(f"Successfully read {len(data)} rows from {filename}")
        return data
    except FileNotFoundError:
        print(f"Error: CSV file '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# 14. Function to append a new line to an existing file
def append_to_file(filename, text):
    """
    Append a new line to an existing file.
    
    Args:
        filename (str): Path to the file
        text (str): Text to append
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')
        print(f"Successfully appended to {filename}")
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False

# 15. Handle file not found error gracefully
def safe_read_file(filename, default_value=""):
    """
    Read a file safely with graceful error handling.
    
    Args:
        filename (str): Path to the file
        default_value (str): Value to return if file not found
        
    Returns:
        str: File contents or default value
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Warning: File '{filename}' not found. Using default value.")
        return default_value
    except PermissionError:
        print(f"Error: Permission denied reading '{filename}'")
        return default_value
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return default_value

# ============================================================================
# PRACTICE PROJECTS
# ============================================================================

# PROJECT 1: Read a log file and count how many times "ERROR" appears
def count_errors_in_log(log_filename):
    """
    Read a log file and count occurrences of "ERROR".
    
    Args:
        log_filename (str): Path to the log file
        
    Returns:
        int: Number of ERROR entries found
        
    Example:
        count = count_errors_in_log("sample.log")
        print(f"Found {count} errors")
    """
    try:
        with open(log_filename, 'r') as file:
            content = file.read()
            error_count = content.count("ERROR")
        print(f"✓ Found {error_count} ERROR entries in {log_filename}")
        return error_count
    except FileNotFoundError:
        print(f"✗ Log file '{log_filename}' not found")
        return 0

# PROJECT 2: Create a contact book that saves to/loads from a file
class ContactBook:
    """
    Simple contact book that saves/loads contacts from a file.
    
    Example:
        book = ContactBook("contacts.txt")
        book.add_contact("Alice", "alice@example.com", "555-1234")
        book.save()
        book.display()
    """
    
    def __init__(self, filename):
        """Initialize contact book with filename."""
        self.filename = filename
        self.contacts = []
        self.load()
    
    def add_contact(self, name, email, phone):
        """Add a contact to the book."""
        contact = {
            "name": name,
            "email": email,
            "phone": phone
        }
        self.contacts.append(contact)
        print(f"✓ Added contact: {name}")
    
    def save(self):
        """Save contacts to file."""
        try:
            with open(self.filename, 'w') as file:
                for contact in self.contacts:
                    line = f"{contact['name']},{contact['email']},{contact['phone']}\n"
                    file.write(line)
            print(f"✓ Saved {len(self.contacts)} contacts to {self.filename}")
            return True
        except Exception as e:
            print(f"✗ Error saving contacts: {e}")
            return False
    
    def load(self):
        """Load contacts from file."""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        self.add_contact(parts[0], parts[1], parts[2])
            print(f"✓ Loaded {len(self.contacts)} contacts from {self.filename}")
        except FileNotFoundError:
            print(f"Note: {self.filename} not found. Starting with empty book.")
    
    def display(self):
        """Display all contacts."""
        print("\n" + "=" * 60)
        print("CONTACT BOOK")
        print("=" * 60)
        for contact in self.contacts:
            print(f"Name:  {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
            print("-" * 60)

# PROJECT 3: Parse CSV data and calculate statistics
def analyze_tickets_from_csv(csv_filename):
    """
    Parse CSV ticket data and calculate statistics.
    
    Args:
        csv_filename (str): Path to CSV file with columns: ticket_id, status, priority, assigned_to, created_date
        
    Returns:
        dict: Statistics including total, by status, by priority
        
    Example:
        stats = analyze_tickets_from_csv("tickets.csv")
        print(f"Total tickets: {stats['total']}")
    """
    import csv
    
    try:
        tickets = []
        status_counts = {}
        priority_counts = {}
        
        with open(csv_filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tickets.append(row)
                
                # Count by status
                status = row['status']
                status_counts[status] = status_counts.get(status, 0) + 1
                
                # Count by priority
                priority = row['priority']
                priority_counts[priority] = priority_counts.get(priority, 0) + 1
        
        stats = {
            "total": len(tickets),
            "by_status": status_counts,
            "by_priority": priority_counts
        }
        
        print(f"✓ Analyzed {stats['total']} tickets from {csv_filename}")
        print(f"  By Status: {stats['by_status']}")
        print(f"  By Priority: {stats['by_priority']}")
        
        return stats
    
    except FileNotFoundError:
        print(f"✗ CSV file '{csv_filename}' not found")
        return None

# PROJECT 4: Generate a summary report and save to file
def generate_summary_report(data_source, output_filename):
    """
    Generate a summary report from sample tickets and save to file.
    
    Args:
        data_source (list): List of ticket dictionaries
        output_filename (str): Path where report will be saved
        
    Example:
        generate_summary_report(sample_tickets, "report.txt")
    """
    try:
        # Calculate statistics
        total_tickets = len(data_source)
        open_tickets = sum(1 for t in data_source if t['status'] == 'open')
        high_priority = sum(1 for t in data_source if t['priority'] == 'high')
        critical_priority = sum(1 for t in data_source if t['priority'] == 'critical')
        
        # Count by assignee
        assignee_counts = {}
        for ticket in data_source:
            assignee = ticket['assigned_to']
            assignee_counts[assignee] = assignee_counts.get(assignee, 0) + 1
        
        # Build report
        report = []
        report.append("=" * 60)
        report.append("TICKET SUMMARY REPORT")
        report.append("=" * 60)
        report.append(f"Generated: May 7, 2026\n")
        
        report.append("OVERVIEW STATISTICS")
        report.append("-" * 60)
        report.append(f"Total Tickets:        {total_tickets}")
        report.append(f"Open Tickets:         {open_tickets}")
        report.append(f"High Priority:        {high_priority}")
        report.append(f"Critical Priority:    {critical_priority}")
        report.append("")
        
        report.append("TICKETS BY ASSIGNEE")
        report.append("-" * 60)
        for assignee, count in sorted(assignee_counts.items(), key=lambda x: x[1], reverse=True):
            report.append(f"{assignee:<20} {count} tickets")
        report.append("")
        
        report.append("OPEN TICKET DETAILS")
        report.append("-" * 60)
        for ticket in data_source:
            if ticket['status'] == 'open':
                report.append(f"ID: {ticket['id']} | Priority: {ticket['priority']:8} | {ticket['description'][:40]}")
        report.append("=" * 60)
        
        # Write report to file
        report_text = '\n'.join(report)
        with open(output_filename, 'w') as file:
            file.write(report_text)
        
        print(f"✓ Report generated and saved to {output_filename}")
        print("\nPreview:")
        print(report_text)
        
        return True
    
    except Exception as e:
        print(f"✗ Error generating report: {e}")
        return False

# ============================================================================
# DEBUGGING TIPS WITH COPILOT
# ============================================================================
"""
USING COPILOT FOR DEBUGGING:

1. HIGHLIGHT ERROR AND ASK COPILOT
   - Select the error message in the console
   - Ask in Chat: "What does this error mean?"
   - Copilot explains the error and suggests fixes
   
   Example:
   Error: TypeError: 'NoneType' object is not subscriptable
   Question: "What does this TypeError mean?"
   
2. RIGHT-CLICK BUGGY CODE → "COPILOT: FIX THIS"
   - Highlight problematic code
   - Right-click → "Copilot: Fix This"
   - Copilot suggests a fix
   
   Example:
   result = my_list[10]  # IndexError if list too short
   → Copilot suggests: if len(my_list) > 10: result = my_list[10]
   
3. ASK COPILOT TO SUGGEST IMPROVEMENTS
   - Paste working code
   - Ask: "How can I improve this code?"
   - Copilot suggests: better error handling, cleaner syntax, better variable names
   
   Example:
   def process(x):
       return x * 2
   
   Improvements:
   - Add docstring
   - Add type hints
   - Add input validation
   - Add error handling

COMMON ERRORS AND HOW TO FIX:

FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
→ Fix: Check file path, use absolute path, handle with try/except

KeyError: 'priority'
→ Fix: Use .get('priority', 'unknown') or check if key exists first

IndexError: list index out of range
→ Fix: Check list length before accessing, use try/except

TypeError: unsupported operand type(s) for +: 'int' and 'str'
→ Fix: Convert to same type: int(x) or str(x)

AttributeError: 'NoneType' object has no attribute 'split'
→ Fix: Check if variable is None before calling methods
"""

