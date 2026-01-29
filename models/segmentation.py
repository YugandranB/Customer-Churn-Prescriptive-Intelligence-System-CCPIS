from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def apply_segmentation(rfm_df):

    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm_df[['Recency','Frequency','Monetary']])

    kmeans = KMeans(n_clusters=4, random_state=42)
    rfm_df['Cluster_ID'] = kmeans.fit_predict(scaled)

    labels = {
        0: "High-Value Loyalist",
        1: "At-Risk VIP",
        2: "Occasional Buyer",
        3: "Dormant/Lost"
    }

    rfm_df['Segment'] = rfm_df['Cluster_ID'].map(labels)

    return rfm_df
