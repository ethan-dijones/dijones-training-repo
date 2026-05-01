#!/usr/bin/env python3
"""
Starter Python Script
Use GitHub Copilot to help write Python code!

Tips for using Copilot with Python:
- Write comments describing what you want the function to do
- Let Copilot suggest the implementation  
- Use Copilot Chat to explain concepts
- Test with print() statements
"""

import json
from datetime import datetime

def main():
    """Main function - program starts here"""
    print("Welcome to Python!")
    
    # Try these Copilot prompts:
    # Create a list of sample ticket dictionaries
    
    # Call functions to test them
    # example: print(format_ticket_id(12345))


# Example Copilot prompts to try in this file:

# 1. Function to format a ticket ID number as "TKT-00000"

# 2. Function to calculate days between two dates

# 3. Function to read ticket data from JSON file

# 4. Function to write ticket data to JSON file

# 5. Function to filter tickets by status (open, closed, pending)


def format_ticket_id(ticket_number):
    """
    Format a ticket number for display
    Let Copilot complete this function
    """
    pass  # Replace this with actual code


def calculate_days_old(created_date):
    """
    Calculate how many days old a ticket is
    
    Args:
        created_date (str): Date string in format "YYYY-MM-DD"
    
    Returns:
        int: Number of days old
    """
    # Let Copilot suggest the implementation
    pass


def load_tickets_from_file(filename):
    """
    Load ticket data from JSON file
    """
    # Copilot prompt: Read JSON file and return list of tickets
    pass


def save_tickets_to_file(tickets, filename):
    """
    Save ticket data to JSON file
    """
    # Copilot prompt: Write tickets list to JSON file with proper formatting
    pass


def filter_tickets(tickets, status):
    """
    Filter tickets by status
    
    Args:
        tickets (list): List of ticket dictionaries
        status (str): Status to filter by ("open", "closed", etc.)
    
    Returns:
        list: Filtered tickets
    """
    # Copilot prompt: Return only tickets matching the given status
    pass


def generate_ticket_report(tickets):
    """
    Generate a summary report from ticket data
    """
    # Copilot prompt: Calculate total, open, closed counts and format as string
    pass


# Example: Working with files
def example_file_operations():
    """Examples of reading and writing files"""
    
    # Write to a text file
    # Copilot prompt: Write list of strings to file, one per line
    
    # Read from a text file  
    # Copilot prompt: Read all lines from file and return as list
    
    pass


# Example: Working with CSV
def example_csv_operations():
    """Examples of reading and writing CSV files"""
    import csv
    
    # Copilot prompt: Read CSV file and return list of dictionaries
    
    # Copilot prompt: Write list of dictionaries to CSV file
    
    pass


# Utility functions

def get_current_timestamp():
    """Return current timestamp as string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_ticket(ticket):
    """Print ticket information in readable format"""
    # Copilot prompt: Format and print ticket dictionary nicely
    pass


# Testing helpers

def create_sample_tickets():
    """
    Create sample ticket data for testing
    """
    # Copilot prompt: Return list of 5 sample ticket dictionaries
    # Each ticket should have: id, status, priority, description, created_date
    pass


def test_functions():
    """Test all functions to make sure they work"""
    print("\n=== Running Tests ===\n")
    
    # Test format_ticket_id
    # print("Test 1:", format_ticket_id(123))
    
    # Test calculate_days_old
    # print("Test 2:", calculate_days_old("2024-04-01"))
    
    # Add more tests here
    print("\n=== Tests Complete ===\n")


# Run the program
if __name__ == "__main__":
    # This runs when you execute the script
    main()
    
    # Uncomment to run tests:
    # test_functions()


"""
Debugging Tips:
- Use print() to check variable values
- Check error messages carefully
- Ask Copilot Chat: "What does this error mean?"
- Break complex problems into smaller functions
- Test each function individually

Common Python mistakes to watch for:
- Indentation errors (Python uses indentation!)
- Forgetting to return values from functions
- Not handling file not found errors
- Mixing tabs and spaces (use spaces only)
"""
