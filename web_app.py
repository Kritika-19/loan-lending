import gradio as gr
from gradio_calendar import Calendar
import sys
import os
sys.path.append(os.path.abspath(os.path.join('.')))
from utils.web_app import predict_defaulter_or_payer

# TODO: If all data is not input, we will throw a warning

def app():

    issue_d = Calendar(label="Issue Date")
    earliest_cr_line = Calendar(label="Earliest Credit Line")
    grade = gr.Dropdown(['A', 'B', 'C', 'D', 'E', 'F', 'G'], label="Loan Grade")
    sub_grade = gr.Dropdown(['A1', 'A2', 'A3', 'A4', 'A5',
                            'B1', 'B2', 'B3', 'B4', 'B5',
                            'C1', 'C2', 'C3', 'C4', 'C5',
                            'D1', 'D2', 'D3', 'D4', 'D5',
                            'E1', 'E2', 'E3', 'E4', 'E5',
                            'F1', 'F2', 'F3', 'F4', 'F5',
                            'G1', 'G2', 'G3', 'G4', 'G5'], label="Loan Subgrade")
    home_ownership = gr.Dropdown(['RENT', 'OWN', 'MORTGAGE', 'OTHER'], label="Home Ownership")
    purpose = gr.Dropdown(['credit_card', 'debt_consolidation', 'car', 'small_business', 
                            'other', 'wedding', 'home_improvement', 'major_purchase', 'medical', 
                            'moving', 'vacation', 'house', 'renewable_energy', 'educational'], label="Purpose of Loan")
    debt_settlement_flag = gr.Dropdown(['Y', 'N'], label="Debt Settlement Flag")
    loan_amnt = gr.Number(label="Loan Amount")
    int_rate = gr.Slider(0, 100, step=0.1, label="Interest Rate")
    installment = gr.Number(label="Installment Amount")
    fico_range_low = gr.Slider(0, 850, step=1,label="FICO Range Low")
    fico_range_high = gr.Slider(0, 850, step=1, label="FICO Range High")
    dti = gr.Number(label="Debt to Income Ratio")
    prediction_label = gr.Textbox(label="AI Ouput")

    # Web App Layout
    with gr.Blocks() as data_block:
        gr.Markdown("# Loan Lending Defaulter Detection")
        gr.Markdown("Fill in the details to check if the person is a defaulter or not.")
        gr.Markdown("## Loan Details")
        with gr.Row():
            loan_amnt.render()
            int_rate.render()
            installment.render()
        with gr.Row():
            grade.render()
            sub_grade.render()

        gr.Markdown("## Lender Details")
        with gr.Row():
            issue_d.render()
            earliest_cr_line.render()
            debt_settlement_flag.render()
        with gr.Row():
            home_ownership.render()
            purpose.render()
            fico_range_low.render()
            fico_range_high.render()
            dti.render()
        gr.Markdown("## Prediction")
        with gr.Row():
            predict_button = gr.Button("Predict")
            prediction_label.render()

        # Mapping the predict button to the function
        predict_button.click(
            fn = predict_defaulter_or_payer,
            inputs = [loan_amnt, int_rate, installment, issue_d, grade, sub_grade, 
                 purpose, debt_settlement_flag, earliest_cr_line,
                 home_ownership, fico_range_low, fico_range_high, dti],
            outputs = prediction_label
        )

    
    return data_block


if __name__ == "__main__":
    app().launch(share=False)
        
        
