def define_user_profile(loan_status):
    # Define user profile based on loan status
    if loan_status in ('Fully Paid', 'Current'):
        return 'Payer'
    else:
        return 'Defaulter'