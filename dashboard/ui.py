import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from intelligence.prescriptive_ai import generate_strategy

def launch_dashboard(model, final_df):

    churners = final_df[final_df['Churn'] == 1].sort_values('Monetary', ascending=False).head(50)
    ids = churners.index.astype(str).tolist()

    def audit(customer_id, api_key):

        row = final_df.loc[float(customer_id)]

        X = np.log1p([[row['Frequency'], row['Monetary'], row['IPT']]])
        prob = model.predict_proba(X)[0][1]

        fig, ax = plt.subplots(figsize=(8,5))
        sns.scatterplot(data=final_df.sample(500),
                        x='Recency',
                        y='Frequency',
                        hue='Segment',
                        ax=ax)

        strategy = generate_strategy(api_key, row)

        return f"{prob:.2%}", fig, strategy

    with gr.Blocks() as app:
        cid = gr.Dropdown(ids, label="Customer ID")
        key = gr.Textbox(type="password")
        btn = gr.Button("Analyze")

        risk = gr.Textbox()
        plot = gr.Plot()
        strategy = gr.Markdown()

        btn.click(audit, [cid,key], [risk,plot,strategy])

    app.launch()
