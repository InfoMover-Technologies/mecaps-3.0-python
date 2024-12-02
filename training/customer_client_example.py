from training.models import CustomerFactory


class CustomerClient:
    @staticmethod
    def main():
        # Create customers using factory
        export_customer = CustomerFactory.new_customer("E")
        local_customer = CustomerFactory.new_customer("L")

        # Set properties for export customer
        export_customer.id = 1
        export_customer.name = "John Export"

        # Set properties for local customer
        local_customer.id = 2
        local_customer.name = "Jane Local"

        # Print customer details
        print("Customer Details:")
        export_customer.print_customer_details()
        local_customer.print_customer_details()

        # Generate credit balance for both customers
        print("\nGenerating Credit Balances:")
        export_customer.generate_credit_balance()
        local_customer.generate_credit_balance()

        # Demonstrate sorting
        customers = [export_customer, local_customer]
        sorted_customers = sorted(customers)

        print("\nSorted Customers by ID:")
        for customer in sorted_customers:
            customer.print_customer_details()

        # Demonstrate error handling with invalid type
        try:
            invalid_customer = CustomerFactory.new_customer("X")
        except ValueError as e:
            print(f"\nError: {e}")


# Run the client
if __name__ == "__main__":
    CustomerClient.main()