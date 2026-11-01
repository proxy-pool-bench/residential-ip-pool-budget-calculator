#!/usr/bin/env python3
"""
Monthly Residential IP Pool Rotation Budget Calculator 2026.
Calculates sustained monthly rotation requirements and average daily burn rate.
"""
import argparse

def calculate_budget(daily_rotations, days, unit_cost):
    total_ips = daily_rotations * days
    total_spend = total_ips * unit_cost
    daily_burn = total_spend / days if days > 0 else 0.0
    return {
        "daily_rotations": daily_rotations,
        "days": days,
        "unit_cost": unit_cost,
        "total_ips": total_ips,
        "total_spend": total_spend,
        "daily_burn": daily_burn
    }

def main():
    parser = argparse.ArgumentParser(description="Residential IP Pool Rotation Budget Calculator")
    parser.add_argument("--daily-rotations", type=int, default=20, help="Required fresh residential IPs per day (default: 20)")
    parser.add_argument("--days", type=int, default=30, help="Operational days per month (default: 30)")
    parser.add_argument("--unit-cost", type=float, default=0.27, help="Discounted cost per residential IP in USD (default: $0.27)")
    args = parser.parse_args()

    res = calculate_budget(args.daily_rotations, args.days, args.unit_cost)
    print(f"Daily Rotation Demand:   {res['daily_rotations']} IPs/day")
    print(f"Total Monthly Quantity:  {res['total_ips']} IPs")
    print(f"Discounted Unit Cost:    ${res['unit_cost']:.2f}/IP")
    print(f"Total Monthly Spend:     ${res['total_spend']:.2f}")
    print(f"Daily Operating Burn:    ${res['daily_burn']:.2f}/day")

if __name__ == "__main__":
    main()
