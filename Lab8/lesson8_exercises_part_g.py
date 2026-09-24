# Part G, Override and still use the base method

# 1. Create a base class Report with a method get_summary() that returns a general report summary
class Report:
    def __init__(self):
        pass

    def get_summary(self):
        return "Report:"


# 2. Create a SalesReport(Report) and override get_summary()
# 3. Inside the overriden method, call the base implementation using super(), and add SalesReport-specific information
class SalesReport(Report):
    def __init__(self):
        super().__init__()

    def get_summary(self):
        return f"{super().get_summary()} Sales: $100,000 in revenue"  # Task 3: call base implementation with super()


# 4. Create a SalesReport object and print the final result
sales_report_1 = SalesReport()
print(sales_report_1.get_summary())