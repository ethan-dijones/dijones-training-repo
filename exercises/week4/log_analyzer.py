"""
Exercise 4.2: File Operations - Log File Analyzer

Objective: Read and write data files

This module demonstrates:
- Reading data from files
- Parsing structured log data
- Filtering and organizing data
- Writing analysis results to output files
"""

def read_log_file(filename):
    """
    Read a log file and return a list of log entries.
    
    Args:
        filename (str): Path to the log file
        
    Returns:
        list: List of log entries (strings)
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []


def parse_log_entry(line):
    """
    Parse a log entry and return dictionary with components.
    
    Expected format: YYYY-MM-DD HH:MM:SS LEVEL Message
    
    Args:
        line (str): A single log line
        
    Returns:
        dict: Dictionary with date, time, level, message
    """
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return None
    
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }


def filter_logs_by_level(entries, level):
    """
    Filter log entries by level (INFO, ERROR, WARNING, etc.).
    
    Args:
        entries (list): List of parsed log entries (dicts)
        level (str): Log level to filter by (e.g., "ERROR", "WARNING")
        
    Returns:
        list: Filtered log entries matching the specified level
    """
    return [entry for entry in entries if entry['level'] == level]


def count_log_levels(entries):
    """
    Count the number of logs for each level.
    
    Args:
        entries (list): List of parsed log entries (dicts)
        
    Returns:
        dict: Dictionary with log levels as keys and counts as values
    """
    level_counts = {}
    for entry in entries:
        level = entry['level']
        level_counts[level] = level_counts.get(level, 0) + 1
    return level_counts


def analyze_logs(filename):
    """
    Analyze log file and return summary statistics and parsed entries.
    
    Args:
        filename (str): Path to the log file
        
    Returns:
        tuple: (stats dict, list of parsed entries)
    """
    lines = read_log_file(filename)
    
    entries = []
    for line in lines:
        entry = parse_log_entry(line)
        if entry:
            entries.append(entry)
    
    stats = count_log_levels(entries)
    stats['total'] = len(entries)
    
    return stats, entries


def generate_detailed_report(entries):
    """
    Generate a detailed analysis report from log entries.
    
    Args:
        entries (list): List of parsed log entries (dicts)
        
    Returns:
        str: Formatted analysis report
    """
    level_counts = count_log_levels(entries)
    
    report = "=" * 50 + "\n"
    report += "LOG ANALYSIS REPORT\n"
    report += "=" * 50 + "\n\n"
    
    report += f"Total Log Entries: {len(entries)}\n\n"
    
    report += "LOG LEVEL BREAKDOWN:\n"
    for level in sorted(level_counts.keys()):
        count = level_counts[level]
        percentage = (count / len(entries)) * 100 if entries else 0
        report += f"  {level:12} : {count:3} entries ({percentage:5.1f}%)\n"
    
    report += "\n" + "-" * 50 + "\n\n"
    
    # Show all ERROR entries
    errors = filter_logs_by_level(entries, "ERROR")
    report += f"CRITICAL ERRORS ({len(errors)} found):\n"
    if errors:
        for error in errors:
            report += f"  [{error['date']} {error['time']}] {error['message']}\n"
    else:
        report += "  No errors found.\n"
    
    report += "\n" + "-" * 50 + "\n\n"
    
    # Show all WARNING entries
    warnings = filter_logs_by_level(entries, "WARNING")
    report += f"WARNINGS ({len(warnings)} found):\n"
    if warnings:
        for warning in warnings:
            report += f"  [{warning['date']} {warning['time']}] {warning['message']}\n"
    else:
        report += "  No warnings found.\n"
    
    report += "\n" + "=" * 50 + "\n"
    
    return report


def write_summary(filename, stats):
    """
    Write log summary to output file.
    
    Args:
        filename (str): Path to the output file
        stats (dict): Statistics dictionary
    """
    try:
        with open(filename, 'w') as f:
            f.write("Log Analysis Summary\n")
            f.write("=" * 30 + "\n")
            f.write(f"Total entries: {stats['total']}\n\n")
            f.write("Breakdown by level:\n")
            for level, count in sorted(stats.items()):
                if level != 'total':
                    f.write(f"  {level}: {count}\n")
        print(f"Summary written to '{filename}'")
    except IOError as error:
        print(f"Error writing to file: {error}")


def write_detailed_report(filename, report_text):
    """
    Write detailed analysis report to output file.
    
    Args:
        filename (str): Path to the output file
        report_text (str): Report content to write
    """
    try:
        with open(filename, 'w') as f:
            f.write(report_text)
        print(f"Detailed report written to '{filename}'")
    except IOError as error:
        print(f"Error writing to file: {error}")


if __name__ == "__main__":
    # Analyze sample log file
    log_file = "sample.log"
    print(f"Analyzing '{log_file}'...\n")
    
    stats, entries = analyze_logs(log_file)
    
    if entries:
        # Print summary
        print(f"Total log entries: {stats['total']}")
        for level in sorted([k for k in stats.keys() if k != 'total']):
            print(f"  {level}: {stats[level]}")
        
        # Write summary to file
        write_summary("log_summary.txt", stats)
        
        # Generate and write detailed report
        detailed_report = generate_detailed_report(entries)
        write_detailed_report("log_analysis_report.txt", detailed_report)
        
        # Display detailed report
        print("\n" + detailed_report)
        
        # Example: Filter and display only errors
        print("\nFiltering example - ERROR entries only:")
        errors = filter_logs_by_level(entries, "ERROR")
        for error in errors:
            print(f"  [{error['date']} {error['time']}] {error['message']}")
    else:
        print("No log entries found or file could not be read.")
