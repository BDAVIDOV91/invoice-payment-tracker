import scripts.query_utils as qu

def main():
    print("All Invoices:")
    all_invoices = qu.get_all_invoices()
    print(all_invoices)

    print("\nOverdue Invoices:")
    overdue_invoices = qu.get_overdue_invoices()
    print(overdue_invoices)

    print("\nPaid Invoices:")
    paid_invoices = qu.get_paid_invoices()
    print(paid_invoices)

if __name__ == "__main__":
    main()