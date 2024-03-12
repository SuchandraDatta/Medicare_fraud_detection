## Medicare Fraud Detection

<h1>Medicare Fraud Detection</h1>
<p>The purpose of this notebook is to perform exploratory data analysis, data preprocessing, feature selection, feature engineering, model training and evaluation for fraud detection using the Medicare Fraud Detection dataset</p>

## Problem Statement
<p><ul><li>USA offers a government backed health insurance program typically for aged individuals to cover their medical bills for hospital visits and treatment.</li>
<li>It has been found that doctors, providers, beneficiaries and associates are involved in unfair practices to augment the claim amount for their benefit. For example, doctors submit claim forms with more sophisticated tests/diagnosis/procedures than was actually performed or using fake patient data so as to receive more insurance payment than rightfully due.
<li>Due to these practices, the insurance providers suffer heavy losses every year which impacts the smooth running of their business. Hence they increase premium payments which makes affordable health care accessible to only the elite few.</li>
<li>Given the dataset with information regarding beneficiaries, inpatients and outpatients, our target is to build a suitable model which can predict how likely a healthcare provider is to perform health insurance fraud
</ul></p>

## Dataset Description
<p>The following is a description of the available attributes of the entities in the dataset. </br>
Note that I did not find any data schema definition so the following is as per my understanding. I spent a lot of time understanding each and every column since understanding the data and the context is the most important step in any data science project. The context here is how US Medicare system and insurance claim filing works and what are the ways this system is exploited.</p>
<h3>Dataset source : <a href="https://data.world/gymprathap/medicare-fraud-detection-dataset">Medicare Fraud Detection Dataset from data.world</a>
</h3>
<ul><li>Provider - Provider ID</li>
<li>PotentialFraud - Yes if provider is possibly fradulent else No</li>
<li> BeneID - Beneficiary ID </li>
<li>DOB	- Date of Birth</li>
<li>DOD	- Date of Death</li>
<li>Gender, Race, State, County - Self explanatory</li>
<li>ChronicCond_Heartfailure, ChronicCond_Alzheimer, ChronicCond_KidneyDisease, ChronicCond_Cancer, ChronicCond_ObstrPulmonary, ChronicCond_Depression, ChronicCond_Diabetes, ChronicCond_IschemicHeart, ChronicCond_Osteoporasis, ChronicCond_rheumatoidarthritis, ChronicCond_stroke
- Binary field of 1/2 to specify if BeneID had these chronic conditions or not
<l1>RenalDiseaseIndicator - 0 if BeneID has no indication of renal diseases else Y </li>
<li>NoOfMonths_PartACov - Medicare system has 4 types of coverage Part A, B, C and D, where under Part A inpatient visits, treatment and nurses is covered. Elgibility for Part A - 65 years minimum, 10 years of full time work</li>
<li>NoOfMonths_PartBCov - Part B covers hospitalization ( admitted to hospital overnight )</li>
<li>IPAnnualReimbursementAmt - amount Medicare will pay for inpatient visits</li>
<li>IPAnnualDeductibleAmt - amount person must pay to Medicare to get the facility of IP annual reimbursement</li>
<li>OPAnnualReimbursementAmt - amount Medicare will pay for outpatient visits</li>
<li>OPAnnualDeductibleAmt - amount person must pay to get annual outpatient reimburesement</li>
<li>ClaimID, ClaimStartDt, ClaimEndDt, Provider - self explanatory</li>
<li>InscClaimAmtReimbursed - how much Medicare paid</li>
<li>AttendingPhysician, OperatingPhysician, OtherPhysician - IDs of the respective physicians</li>
<li>AdmissionDt - Date of admission</li>
<li>ClmAdmitDiagnosisCode - What was the diagnosis code assigned when patient was admitted ?</li>
<li>DeductibleAmtPaid - amount person actually paid as opposed to the previous attributed OPAnnualDeductibleAmt which is how much he was supposed to pay</li>
<li>DischargeDt - date of discharge for outpatients</li>
<li>DiagnosisGroupCode - used to categorize inpatient visits</li>
<li>ClmDiagnosisCode_1 to ClmDiagnosisCode_10 - There is an official categorization of diseases called ICD or International Classification of Diseases. Diagnosis Code 1 is the most important diagnosis specifying which is the major dieases, subsequent codes are for subsequent diagnoses. Based on the codes given it looks like it is using ICD 9. This is most important attribute as this specifies the disease in terms of medical coding and any mistake here will lead to rejection of the claim form.
<li>ClmProcedureCode_1 to ClmProcedureCode_6 - Codes for the procedure which was allegedly performed given the diagnosis code</li>


## Contents of repository
<li>Notebook containing EDA, feature engineering, feature selection, model building and evaluation</li>
<li>Inference script to generate predictions on any given data</li>
<li>Model predictions on unseen data stored in the Excel file</li>
<li>List of dependencies and their versions</li>
