import pandas as pd
import json
import pickle
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import pickle

def calculate_age(birthdate, claimdate):
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        enddate = datetime.strptime(claimdate, '%Y-%m-%d')
        age = enddate.year - birthdate.year - ((enddate.month, enddate.day) < (birthdate.month, birthdate.day))
        return age

def create_consolidated_dataset():
        target_variable_df = pd.read_csv("/content/data/dataset/Test-1542969243754.csv")
        inpatient_df = pd.read_csv("/content/data/dataset/Test_Inpatientdata-1542969243754.csv")
        outpatient_df = pd.read_csv("/content/data/dataset/Test_Outpatientdata-1542969243754.csv")
        beneficiary_df = pd.read_csv("/content/data/dataset/Test_Beneficiarydata-1542969243754.csv")
        target_inpatient_df = pd.merge(target_variable_df, inpatient_df,on='Provider')
        target_inpatient_beneficiary_df = pd.merge(target_inpatient_df, beneficiary_df,on='BeneID')

        target_outpatient_df = pd.merge(target_variable_df, outpatient_df, on='Provider')
        target_outpatient_beneficiary_df = pd.merge(target_outpatient_df, beneficiary_df, on='BeneID')

        target_inpatient_beneficiary_df['patient_type']=['inpatient']*len(target_inpatient_beneficiary_df)
        target_outpatient_beneficiary_df['patient_type']=['outpatient']*len(target_outpatient_beneficiary_df)

        dataset = pd.concat([target_inpatient_beneficiary_df, target_outpatient_beneficiary_df])
        dataset = dataset[dataset['ClmDiagnosisCode_1'].notna()]
        dataset['age'] = dataset.apply(lambda x:calculate_age(x['DOB'],x['ClaimEndDt']), axis=1)
        return dataset

def load_model():
      with open("model.pkl", "rb") as fptr:
            model = pickle.loads(fptr.read())
      return model
def load_metadata():
      with open("metadata.json","r") as fptr:
            data = json.loads(fptr.read())
      return data
def load_scaling_metadata():
    with open("scaling_metadata.pkl","rb") as fptr:
            data = pickle.loads(fptr.read())
    return data

def add_new_features(dataset):
        dataset['patient_type_flag'] = dataset['patient_type'].apply(lambda x:1 if x=='inpatient' else 0)
        dataset['gender_flag'] = dataset['Gender'].apply(lambda x:1 if x==1 else 0)
        with open("metadata.json","r") as fptr:
                metadata = json.loads(fptr.read())
        for each in dataset['Race'].unique():
              dataset['race_is_{}'.format(each)] = dataset['Race'].apply(lambda x:1 if x==each else 0)
        dataset['is_state_in_top_5_fraud_states'] = dataset['State'].apply(lambda x:1 if x in metadata["top_5_states"] else 0)
        dataset['is_county_in_top_5_fraud_county'] = dataset['County'].apply(lambda x:1 if x in metadata["top_5_county"] else 0)
        dataset['is_claim_diagnosis_code_1_in_top_5_codes'] = dataset['ClmDiagnosisCode_1'].apply(lambda x:1 if x in metadata["top_5_codes"] else 0)
        return dataset
def adjust_existing_features(dataset):
      for each in dataset.columns:
          if "ChronicCond_" in each:
                dataset[each+"_adjusted"] = dataset[each].apply(lambda x:x-1)
      dataset['RenalDiseaseIndicator'] = dataset['RenalDiseaseIndicator'].apply(lambda x:1 if x.lower()=='y' else 0)
      return dataset

data = create_consolidated_dataset()
data = add_new_features(data)
data = adjust_existing_features(data)
data['DeductibleAmtPaid'] = data['DeductibleAmtPaid'].interpolate(method='linear')
data_ready_for_infer = data[['InscClaimAmtReimbursed','DeductibleAmtPaid','RenalDiseaseIndicator',\
        'age', 'patient_type_flag', 'gender_flag', 'race_is_1', 'race_is_2',\
         'race_is_5', 'race_is_3', 'is_state_in_top_5_fraud_states',\
         'is_county_in_top_5_fraud_county','is_claim_diagnosis_code_1_in_top_5_codes',\
         'ChronicCond_Alzheimer_adjusted', 'ChronicCond_Heartfailure_adjusted',\
         'ChronicCond_KidneyDisease_adjusted', 'ChronicCond_Cancer_adjusted',\
         'ChronicCond_ObstrPulmonary_adjusted',\
         'ChronicCond_Depression_adjusted', 'ChronicCond_Diabetes_adjusted',\
         'ChronicCond_IschemicHeart_adjusted','ChronicCond_Osteoporasis_adjusted',\
         'ChronicCond_rheumatoidarthritis_adjusted','ChronicCond_stroke_adjusted' ]]
data_ready_for_infer = data_ready_for_infer.dropna()
model = load_model()
scaler = load_scaling_metadata()
output_df = data_ready_for_infer
data_ready_for_infer = scaler.transform(data_ready_for_infer)
predictions = model.predict(data_ready_for_infer)
print(predictions)
output_df.loc[:,'prediction'] = predictions
output_df.to_excel("test_file_with_prediction.xlsx")