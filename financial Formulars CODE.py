# financial formulars to use and their concepts Breifly


'''
1 Compound Interest Formula:

The compound interest formula is used to calculate the interest earned on an investment over a period of time. 
It takes into account both the principal amount and the interest earned over a certain period of time. The formula is given as:

A = P(1 + r/n)^(nt)

where A is the total amount, P is the principal amount, r is the interest rate,
n is the number of times interest is compounded per year, and t is the time period.



2 Present Value Formula:

The present value formula is used to calculate the current value of a future payment or investment. 
It takes into account the time value of money and is often used in financial planning. The formula is given as:

PV = FV / (1 + r)^t

where PV is the present value, FV is the future value, r is the interest rate, and t is the time period.



3 Net Present Value (NPV) Formula:

The net present value formula is used to determine the value of an investment by calculating the 
present value of its future cash flows, minus the initial cost of the investment. The formula is given as:

NPV = -C0 + ∑(Ct / (1 + r)^t)

where NPV is the net present value, C0 is the initial cost of the investment, Ct is the cash flow for each time period, and r is the discount rate.



4 Return on Investment (ROI) Formula:

The return on investment formula is used to determine the amount of return on an investment, expressed as a percentage of the original investment.
The formula is given as:

ROI = (Gain from Investment - Cost of Investment) / Cost of Investment

where ROI is the return on investment, Gain from Investment is the amount gained from the investment, and Cost of Investment is the initial cost of the investment.



5 Debt-to-Equity Ratio Formula:

The debt-to-equity ratio formula is used to measure the proportion of debt financing a company uses compared to equity financing. It is calculated as:

Debt-to-Equity Ratio = Total Debt / Total Equity

where Total Debt is the total amount of debt a company has and Total Equity is the total amount of equity the company has.

'''


# CODE

class FinancialFormulas:
    def compound_interest(self, principal, interest_rate, time, compounds_per_year):
        amount = principal * (1 + (interest_rate/compounds_per_year))**(compounds_per_year*time)
        return amount
    
    def present_value(self, future_value, interest_rate, time):
        present_value = future_value / (1 + interest_rate)**time
        return present_value
    
    def net_present_value(self, initial_cost, cash_flows, discount_rate):
        npv = -initial_cost
        for t, cash_flow in enumerate(cash_flows):
            npv += cash_flow / (1 + discount_rate)**(t+1)
        return npv
    
    def return_on_investment(self, initial_cost, final_value):
        roi = (final_value - initial_cost) / initial_cost
        return roi
    
    def debt_to_equity_ratio(self, total_debt, total_equity):
        ratio = total_debt / total_equity
        return ratio
'''
To use this class, you can create an instance of the FinancialFormulas class and call its methods to calculate the desired 
financial formula. Here's an example:
'''

ff = FinancialFormulas()

# Calculate the compound interest on a $1000 investment with a 5% annual interest rate, compounded quarterly for 3 years
amount = ff.compound_interest(principal=1000, interest_rate=0.05, time=3, compounds_per_year=4)
print(f"Amount after 3 years of quarterly compounding: ${amount:.2f}")

# Calculate the present value of a $1000 payment 5 years from now, with a 4% discount rate
present_value = ff.present_value(future_value=1000, interest_rate=0.04, time=5)
print(f"Present value of $1000 in 5 years: ${present_value:.2f}")

# Calculate the net present value of an investment with an initial cost of $500, expected cash flows of $100, $200, and $300 in years 1, 2, and 3, and a discount rate of 6%
npv = ff.net_present_value(initial_cost=500, cash_flows=[100, 200, 300], discount_rate=0.06)
print(f"Net present value of investment: ${npv:.2f}")

# Calculate the return on investment for an investment with an initial cost of $1000 and a final value of $1500
roi = ff.return_on_investment(initial_cost=1000, final_value=1500)
print(f"Return on investment: {roi*100:.2f}%")

# Calculate the debt-to-equity ratio for a company with $1,000,000 in debt and $2,000,000 in equity
ratio = ff.debt_to_equity_ratio(total_debt=1000000, total_equity=2000000)
print(f"Debt-to-equity ratio: {ratio:.2f}")


























