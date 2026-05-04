# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# ---------------------------------------------------------
# TODO 1: Service categories and rates
# ---------------------------------------------------------
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Migration": 200,
    "Cybersecurity Audit": 225,
    "IT Support": 100
}

# ---------------------------------------------------------
# TODO 2: Customer dictionaries
# ---------------------------------------------------------
customer1 = {
    "company_name": "Alpha Innovations",
    "contact_person": "Sarah Lee",
    "email": "slee@alphainnov.com",
    "phone": "555-1001"
}

customer2 = {
    "company_name": "BrightPath Logistics",
    "contact_person": "Michael Torres",
    "email": "mtorres@brightpath.com",
    "phone": "555-2002"
}

customer3 = {
    "company_name": "Cobalt Manufacturing",
    "contact_person": "Dana Kim",
    "email": "dkim@cobalt.com",
    "phone": "555-3003"
}

customer4 = {
    "company_name": "Delta Finance Group",
    "contact_person": "Robert Chen",
    "email": "rchen@deltafinance.com",
    "phone": "555-4004"
}

# ---------------------------------------------------------
# TODO 3: Master customers dictionary
# ---------------------------------------------------------
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# ---------------------------------------------------------
# TODO 4: Display all customers
# ---------------------------------------------------------
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(f"{cid}: {info}")

# ---------------------------------------------------------
# TODO 5: Customer lookups
# ---------------------------------------------------------
print("\n\nCustomer Lookups:")
print("-" * 60)

c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("C002 Info:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Lookup:", c999_info)

# ---------------------------------------------------------
# TODO 6: Update customer information
# ---------------------------------------------------------
print("\n\nUpdating Customer Information:")
print("-" * 60)

customers["C001"]["phone"] = "555-1111"
customers["C002"]["industry"] = "Logistics"

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# ---------------------------------------------------------
# TODO 7: Project dictionaries
# ---------------------------------------------------------
project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 40, "budget": 6000}
project2 = {"name": "Data Cleanup", "service": "Data Analysis", "hours": 25, "budget": 5000}
project3 = {"name": "Cloud Migration Phase 1", "service": "Cloud Migration", "hours": 60, "budget": 12000}
project4 = {"name": "Security Audit", "service": "Cybersecurity Audit", "hours": 30, "budget": 8000}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [],
    "C004": [project4]
}

print("\n\nProject Information:")
print("-" * 60)
for cid, plist in projects.items():
    print(cid, plist)

# ---------------------------------------------------------
# TODO 8: Project cost calculations
# ---------------------------------------------------------
print("\n\nProject Cost Calculations:")
print("-" * 60)

for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print(f"{cid} - {p['name']}: Cost = ${cost}")

# ---------------------------------------------------------
# TODO 9: Customer statistics
# ---------------------------------------------------------
print("\n\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", list(customers.keys()))
print("Customer Companies:", [c["company_name"] for c in customers.values()])
print("Total Customers:", len(customers))

# ---------------------------------------------------------
# TODO 10: Service usage analysis
# ---------------------------------------------------------
print("\n\nService Usage Analysis:")
print("-" * 60)

service_counts = {}
for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print(service_counts)

# ---------------------------------------------------------
# TODO 11: Financial aggregations
# ---------------------------------------------------------
print("\n\nFinancial Summary:")
print("-" * 60)

all_projects = [p for plist in projects.values() for p in plist]

total_hours = sum(p["hours"] for p in all_projects)
total_budget = sum(p["budget"] for p in all_projects)
avg_budget = total_budget / len(all_projects) if all_projects else 0
max_budget = max(p["budget"] for p in all_projects)
min_budget = min(p["budget"] for p in all_projects)

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Most Expensive Project:", max_budget)
print("Least Expensive Project:", min_budget)

# ---------------------------------------------------------
# TODO 12: Customer summary report
# ---------------------------------------------------------
print("\n\nCustomer Summary Report:")
print("-" * 60)

for cid, info in customers.items():
    plist = projects[cid]
    total_hours = sum(p["hours"] for p in plist)
    total_budget = sum(p["budget"] for p in plist)
    print(f"{cid} - {info['company_name']}")
    print(" Projects:", len(plist))
    print(" Total Hours:", total_hours)
    print(" Total Budget:", total_budget)
    print()

# ---------------------------------------------------------
# TODO 13: Adjusted service rates
# ---------------------------------------------------------
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)

adjusted_rates = {s: r * 1.1 for s, r in services.items()}
print(adjusted_rates)

# ---------------------------------------------------------
# TODO 14: Active customers
# ---------------------------------------------------------
print("\n\nActive Customers (with projects):")
print("-" * 60)

active_customers = {cid: info for cid, info in customers.items() if len(projects[cid]) > 0}
print(active_customers)

# ---------------------------------------------------------
# TODO 15: Customer budget totals
# ---------------------------------------------------------
print("\n\nCustomer Budget Totals:")
print("-" * 60)

customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}
print(customer_budgets)

# ---------------------------------------------------------
# TODO 16: Service pricing tiers
# ---------------------------------------------------------
print("\n\nService Pricing Tiers:")
print("-" * 60)

service_tiers = {
    s: ("Premium" if r >= 200 else "Standard" if r >= 100 else "Basic")
    for s, r in services.items()
}
print(service_tiers)

# ---------------------------------------------------------
# TODO 17: Customer validation
# ---------------------------------------------------------
print("\n\nCustomer Validation:")
print("-" * 60)

def validate_customer(c):
    required = ["company_name", "contact_person", "email", "phone"]
    return all(field in c for field in required)

for cid, info in customers.items():
    print(cid, validate_customer(info))

# ---------------------------------------------------------
# TODO 18: Project status tracking
# ---------------------------------------------------------
print("\n\nProject Status Summary:")
print("-" * 60)

# Add status fields
statuses = ["active", "completed", "pending"]
i = 0
for plist in projects.values():
    for p in plist:
        p["status"] = statuses[i % 3]
        i += 1

status_counts = {}
for plist in projects.values():
    for p in plist:
        s = p["status"]
        status_counts[s] = status_counts.get(s, 0) + 1

print(status_counts)

# ---------------------------------------------------------
# TODO 19: Budget analysis function
# ---------------------------------------------------------
print("\n\nDetailed Budget Analysis:")
print("-" * 60)

def analyze_customer_budgets(projects_dict):
    results = {}
    for cid, plist in projects_dict.items():
        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count else 0
        results[cid] = {"total": total, "average": avg, "count": count}
    return results

print(analyze_customer_budgets(projects))

# ---------------------------------------------------------
# TODO 20: Service recommendation system
# ---------------------------------------------------------
print("\n\nService Recommendations:")
print("-" * 60)

def recommend_services(customer_id, customers, projects, services):
    used = {p["service"] for p in projects[customer_id]}
    unused = [s for s in services if s not in used]

    # Estimate budget range
    budgets = [p["budget"] for p in projects[customer_id]]
    avg_budget = sum(budgets) / len(budgets) if budgets else 0

    # Recommend services priced near their typical budget
    recommended = [s for s in unused if services[s] * 10 <= avg_budget + 5000]
    return recommended

for cid in customers:
    print(cid, recommend_services(cid, customers, projects, services))