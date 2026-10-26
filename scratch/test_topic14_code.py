import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

print("=== 1. PROBABILITY FUNDAMENTALS & CONTINGENCY TABLE ===")
# 100 emails: 20 Spam, 80 Ham
n_total = 100
n_spam = 20
n_ham = 80

p_spam = n_spam / n_total
p_ham = n_ham / n_total
print(f"P(Spam) = {n_spam}/{n_total} = {p_spam:.4f}")
print(f"P(Ham)  = {n_ham}/{n_total} = {p_ham:.4f}")

# Word 'free'
# In Spam: 16 contain 'free', 4 do not
# In Ham:   8 contain 'free', 72 do not
spam_free = 16
spam_nofree = 4
ham_free = 8
ham_nofree = 72

total_free = spam_free + ham_free
total_nofree = spam_nofree + ham_nofree
p_free = total_free / n_total
print(f"Total 'free' = {total_free}, P(Free) = {total_free}/{n_total} = {p_free:.4f}")

# Joint probabilities
p_spam_and_free = spam_free / n_total
p_ham_and_free = ham_free / n_total
print(f"P(Spam and Free) = {spam_free}/{n_total} = {p_spam_and_free:.4f}")
print(f"P(Ham and Free)  = {ham_free}/{n_total} = {p_ham_and_free:.4f}")

# Conditional probabilities (Likelihoods)
p_free_given_spam = spam_free / n_spam
p_free_given_ham = ham_free / n_ham
print(f"P(Free | Spam) = {spam_free}/{n_spam} = {p_free_given_spam:.4f} (Likelihood under Spam)")
print(f"P(Free | Ham)  = {ham_free}/{n_ham} = {p_free_given_ham:.4f} (Likelihood under Ham)")

print("\n=== 2. BAYES' THEOREM VERIFICATION ===")
# P(Spam | Free) = [P(Free | Spam) * P(Spam)] / P(Free)
numerator_spam = p_free_given_spam * p_spam
p_spam_given_free = numerator_spam / p_free
print(f"Numerator: P(Free|Spam) * P(Spam) = {p_free_given_spam:.2f} * {p_spam:.2f} = {numerator_spam:.4f}")
print(f"Denominator: P(Free) = {p_free:.4f}")
print(f"Posterior P(Spam | Free) = {numerator_spam:.4f} / {p_free:.4f} = {p_spam_given_free:.4f} ({p_spam_given_free*100:.2f}%)")

numerator_ham = p_free_given_ham * p_ham
p_ham_given_free = numerator_ham / p_free
print(f"Posterior P(Ham | Free)  = {numerator_ham:.4f} / {p_free:.4f} = {p_ham_given_free:.4f} ({p_ham_given_free*100:.2f}%)")
assert np.isclose(p_spam_given_free + p_ham_given_free, 1.0)
print(f"Check sum to 1: {p_spam_given_free:.4f} + {p_ham_given_free:.4f} = {p_spam_given_free + p_ham_given_free:.4f}")

print("\n=== 3. MULTI-FEATURE NAIVE BAYES WORKED EXAMPLE ===")
# 3 words: 'free', 'offer', 'prize'
# Training counts:
# Spam (20 total): free=16, offer=14, prize=10
# Ham (80 total):  free=8,  offer=12, prize=4
p_offer_given_spam = 14 / 20  # 0.70
p_offer_given_ham  = 12 / 80  # 0.15
p_prize_given_spam = 10 / 20  # 0.50
p_prize_given_ham  = 4  / 80  # 0.05

print(f"Spam likelihoods: Free={p_free_given_spam:.2f}, Offer={p_offer_given_spam:.2f}, Prize={p_prize_given_spam:.2f}")
print(f"Ham likelihoods:  Free={p_free_given_ham:.2f}, Offer={p_offer_given_ham:.2f}, Prize={p_prize_given_ham:.2f}")

# Test email with all 3 words:
likelihood_spam = p_free_given_spam * p_offer_given_spam * p_prize_given_spam
likelihood_ham  = p_free_given_ham * p_offer_given_ham * p_prize_given_ham
print(f"Likelihood P(X | Spam) = 0.80 * 0.70 * 0.50 = {likelihood_spam:.6f}")
print(f"Likelihood P(X | Ham)  = 0.10 * 0.15 * 0.05 = {likelihood_ham:.6f}")

unnorm_score_spam = likelihood_spam * p_spam
unnorm_score_ham  = likelihood_ham * p_ham
print(f"Unnormalized Score(Spam) = {likelihood_spam:.4f} * {p_spam:.2f} = {unnorm_score_spam:.6f}")
print(f"Unnormalized Score(Ham)  = {likelihood_ham:.6f} * {p_ham:.2f} = {unnorm_score_ham:.6f}")

total_score = unnorm_score_spam + unnorm_score_ham
post_spam = unnorm_score_spam / total_score
post_ham  = unnorm_score_ham / total_score
print(f"Normalized Posterior P(Spam | X) = {unnorm_score_spam:.6f} / {total_score:.6f} = {post_spam:.6f} ({post_spam*100:.2f}%)")
print(f"Normalized Posterior P(Ham | X)  = {unnorm_score_ham:.6f} / {total_score:.6f} = {post_ham:.6f} ({post_ham*100:.2f}%)")

print("\n=== 4. ZERO FREQUENCY & LAPLACE SMOOTHING ===")
# Word 'jackpot': Count in Spam = 4, Count in Ham = 0
# Unsmoothed:
p_jackpot_given_ham_raw = 0 / 80
score_ham_raw = unnorm_score_ham * p_jackpot_given_ham_raw
print(f"Raw P(jackpot | Ham) = 0/80 = 0.0 -> Score(Ham) drops to {score_ham_raw:.6f} (ZERO COLLAPSE)")

# Laplace smoothing (alpha=1, K=2 for binary presence)
# formula: (count + alpha) / (N_class + alpha * K)
alpha = 1.0
K = 2
p_free_s_spam = (16 + alpha) / (20 + alpha * K)
p_offer_s_spam = (14 + alpha) / (20 + alpha * K)
p_prize_s_spam = (10 + alpha) / (20 + alpha * K)
p_jackpot_s_spam = (4 + alpha) / (20 + alpha * K)

p_free_s_ham = (8 + alpha) / (80 + alpha * K)
p_offer_s_ham = (12 + alpha) / (80 + alpha * K)
p_prize_s_ham = (4 + alpha) / (80 + alpha * K)
p_jackpot_s_ham = (0 + alpha) / (80 + alpha * K)

print(f"Smoothed P(jackpot | Spam) = (4+1)/(20+2) = 5/22 = {p_jackpot_s_spam:.4f}")
print(f"Smoothed P(jackpot | Ham)  = (0+1)/(80+2) = 1/82 = {p_jackpot_s_ham:.4f}")

smoothed_score_spam = p_spam * p_free_s_spam * p_offer_s_spam * p_prize_s_spam * p_jackpot_s_spam
smoothed_score_ham  = p_ham * p_free_s_ham * p_offer_s_ham * p_prize_s_ham * p_jackpot_s_ham
norm_smoothed_spam = smoothed_score_spam / (smoothed_score_spam + smoothed_score_ham)
norm_smoothed_ham  = smoothed_score_ham / (smoothed_score_spam + smoothed_score_ham)
print(f"Smoothed Score(Spam) = {smoothed_score_spam:.8f}")
print(f"Smoothed Score(Ham)  = {smoothed_score_ham:.8f}")
print(f"Smoothed Posterior P(Spam | X_new) = {norm_smoothed_spam:.6f} ({norm_smoothed_spam*100:.2f}%)")
print(f"Smoothed Posterior P(Ham | X_new)  = {norm_smoothed_ham:.6f} ({norm_smoothed_ham*100:.2f}%)")

print("\n=== 5. COMPLETE PYTHON LAB: SPAM CLASSIFIER (MULTINOMIALNB) ===")
# Synthetic but rich, reproducible dataset of 80 messages (40 Spam, 40 Ham)
data = [
    # 40 Spam emails
    ("Urgent: Claim your free prize and cash bonus now!", 1),
    ("Congratulations! You won a guaranteed lottery cash prize", 1),
    ("Free gift card and exclusive promotion reward awaits you", 1),
    ("Winner! Claim your urgent cash jackpot immediately", 1),
    ("Exclusive deal: Get free trial and big discount offer", 1),
    ("Urgent account verification required to receive cash prize", 1),
    ("Get your free luxury watch today with special offer", 1),
    ("Special promo: Free coins and fast lottery cash reward", 1),
    ("Instant cash payout! Click here to claim your reward", 1),
    ("Unlimited free credits and holiday prize voucher", 1),
    ("You have been selected for a free cash transfer bonus", 1),
    ("Claim urgent lottery prize before promotion expires tonight", 1),
    ("Risk free investment with guaranteed double cash returns", 1),
    ("Win big money today! Free tickets and jackpot tokens", 1),
    ("Urgent notice: Claim your complimentary bonus voucher now", 1),
    ("Get cheap medication online with free shipping and bonus", 1),
    ("Congratulations winner! Your cash prize is ready to claim", 1),
    ("Exclusive discount: 90% off luxury items plus free gift", 1),
    ("Hot crypto opportunity! Free tokens and instant cash profit", 1),
    ("Urgent security alert: Verify your bank for cash reward", 1),
    ("Double your income working from home! Free starter kit", 1),
    ("Limited time offer: Free smartphone reward for lucky winner", 1),
    ("You won the international sweepstakes! Claim jackpot prize", 1),
    ("Fast easy cash loans approved instantly! Zero interest offer", 1),
    ("Free sample box and bonus shopping vouchers delivered today", 1),
    ("Urgent payout pending: Confirm account to release prize money", 1),
    ("Claim your free VIP membership and luxury vacation voucher", 1),
    ("Selected winner notification: Collect your $5000 prize award", 1),
    ("Secret cash formula revealed! Get your free access guide", 1),
    ("Instant lottery winner: Check your winning ticket numbers now", 1),
    ("Exclusive reward points! Redeem for free gift cards online", 1),
    ("Urgent: Free credit score repair and guaranteed cash bonus", 1),
    ("Get rich quick with automated bot! Free registration today", 1),
    ("Winner confirmed! Collect your free shopping spree prize", 1),
    ("Urgent message regarding your unclaimed cash lottery reward", 1),
    ("Complimentary flight ticket voucher and luxury hotel prize", 1),
    ("Free entries to the annual mega jackpot prize draw tonight", 1),
    ("Special rebate reward: Claim your free cash back transfer", 1),
    ("Congratulations! Selected for free tech gadget gift giveaway", 1),
    ("Urgent bank transfer of lottery prize funds requires approval", 1),

    # 40 Ham (Legitimate) emails
    ("Hi team, please find the attached weekly project progress report", 0),
    ("Quarterly financial budget review meeting scheduled for tomorrow afternoon", 0),
    ("Could you please review the updated Python codebase and pull request?", 0),
    ("Meeting notes from today's client consultation and discussion", 0),
    ("Can we reschedule our engineering standup to Thursday at 10 AM?", 0),
    ("Please submit your quarterly project status report by end of day", 0),
    ("Team lunch planned for Friday to celebrate project milestone completion", 0),
    ("Attached is the invoice for software design services rendered in March", 0),
    ("Here is the updated project documentation and API endpoint schema", 0),
    ("Reminder: Submit your timesheets and holiday requests before Friday", 0),
    ("Thanks for your insightful feedback on the machine learning pipeline", 0),
    ("The database migration script finished successfully without errors", 0),
    ("Customer support ticket #492 has been resolved and closed today", 0),
    ("Draft proposal for the upcoming product roadmap is ready for review", 0),
    ("Let us discuss the quarterly metrics during the tomorrow morning call", 0),
    ("Could you send the updated slide deck for the client presentation?", 0),
    ("The server maintenance downtime is scheduled for midnight this Sunday", 0),
    ("Great presentation at the conference yesterday! Loved the insights", 0),
    ("Please verify the git pull request merge into the main development branch", 0),
    ("Annual employee performance review forms are due by next Wednesday", 0),
    ("Summary of user research interviews and key usability findings", 0),
    ("Please sign the contractor agreement and return it to human resources", 0),
    ("The frontend UI component bug has been identified and patched", 0),
    ("Agenda for tomorrow's cross-functional engineering team workshop", 0),
    ("Quarterly revenue analysis and sales forecast sheet attached", 0),
    ("Thank you for sharing the research paper on neural network optimization", 0),
    ("Please remember to update your team task status on the project board", 0),
    ("We need to order new monitor cables and adapters for the office desks", 0),
    ("Feedback on your clean code refactoring: overall looks very structured", 0),
    ("The security audit report has been published to the internal team wiki", 0),
    ("Can we sync for 15 minutes regarding the API response latency issue?", 0),
    ("Attached are the finalized architectural blueprints for the cloud deployment", 0),
    ("Friendly reminder: All-hands company meeting will start at 3 PM today", 0),
    ("Please review the proposed sprint goals before our planning session", 0),
    ("The new intern begins on Monday, let us prepare the onboarding guide", 0),
    ("Here are the test coverage results from the continuous integration run", 0),
    ("Could you provide access to the analytics dashboard for the marketing team?", 0),
    ("Minutes of meeting from the executive leadership sync have been posted", 0),
    ("Please double-check the billing address on the vendor invoice file", 0),
    ("Looking forward to collaborating with your department on the upcoming sprint", 0)
]

df = pd.DataFrame(data, columns=['text', 'label'])
print(f"Dataset shape: {df.shape}")
print(f"Class distribution: Ham(0)={sum(df['label']==0)}, Spam(1)={sum(df['label']==1)}")

# Train/Test split: 75/25 stratified
X_train_text, X_test_text, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.25, random_state=42, stratify=df['label']
)
print(f"Train samples: {len(X_train_text)} (Ham: {sum(y_train==0)}, Spam: {sum(y_train==1)})")
print(f"Test samples:  {len(X_test_text)} (Ham: {sum(y_test==0)}, Spam: {sum(y_test==1)})")

# Train pipeline: CountVectorizer + MultinomialNB
spam_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english', lowercase=True)),
    ('nb', MultinomialNB(alpha=1.0))
])

spam_pipeline.fit(X_train_text, y_train)
y_pred = spam_pipeline.predict(X_test_text)
y_proba = spam_pipeline.predict_proba(X_test_text)

acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"\nMultinomialNB Test Metrics (alpha=1.0):")
print(f"  Accuracy:  {acc:.4f} ({acc*100:.1f}%)")
print(f"  Precision: {prec:.4f} ({prec*100:.1f}%)")
print(f"  Recall:    {rec:.4f} ({rec*100:.1f}%)")
print(f"  F1-Score:  {f1:.4f} ({f1*100:.1f}%)")
print(f"Confusion Matrix (TN, FP / FN, TP):\n{cm}")
tn, fp, fn, tp = cm.ravel()
print(f"  TN={tn}, FP={fp}, FN={fn}, TP={tp}")

# Sample test messages with predictions
test_examples = [
    "Claim your free prize and cash bonus today!",
    "Team meeting scheduled for Monday project review",
    "Urgent account update required to verify funds",
    "Please find attached the financial report invoice"
]
ex_preds = spam_pipeline.predict(test_examples)
ex_probs = spam_pipeline.predict_proba(test_examples)

print("\nPredictions on Unseen Messages:")
for msg, pred, prob in zip(test_examples, ex_preds, ex_probs):
    lbl = "Spam" if pred == 1 else "Ham"
    print(f"  Text: '{msg}'")
    print(f"    -> Predicted: {lbl} | P(Ham)={prob[0]:.4f}, P(Spam)={prob[1]:.4f}")

# Effect of smoothing alpha:
print("\nSmoothing Alpha Comparison on ambiguous sample 'Free urgent ticket':")
ambig_sample = ["Free urgent ticket"]
for a in [0.001, 0.1, 1.0, 5.0, 20.0]:
    p = Pipeline([
        ('vec', CountVectorizer(stop_words='english', lowercase=True)),
        ('nb', MultinomialNB(alpha=a))
    ])
    p.fit(X_train_text, y_train)
    probs = p.predict_proba(ambig_sample)[0]
    print(f"  alpha={a:6.3f} -> P(Ham)={probs[0]:.4f}, P(Spam)={probs[1]:.4f}")

print("\n=== 6. GAUSSIAN NAIVE BAYES LAB (GAUSSIANNB) ===")
# Synthetic numerical dataset: Student Exam Performance (2 continuous features)
# Feature 1: Study Hours per week (Gaussian per class)
# Feature 2: Practice Quiz Score % (Gaussian per class)
# Class 0: Not Passed (40 samples, mean hours=12, quiz=55)
# Class 1: Passed     (40 samples, mean hours=28, quiz=82)
np.random.seed(42)
n_gauss_each = 40

hours_c0 = np.random.normal(loc=12.5, scale=3.2, size=n_gauss_each)
quiz_c0  = np.random.normal(loc=54.0, scale=7.5, size=n_gauss_each)
y_g0 = np.zeros(n_gauss_each, dtype=int)

hours_c1 = np.random.normal(loc=27.5, scale=3.8, size=n_gauss_each)
quiz_c1  = np.random.normal(loc=81.5, scale=6.8, size=n_gauss_each)
y_g1 = np.ones(n_gauss_each, dtype=int)

X_hours = np.clip(np.concatenate([hours_c0, hours_c1]), 2.0, 45.0)
X_quiz  = np.clip(np.concatenate([quiz_c0, quiz_c1]), 25.0, 100.0)
X_gauss = np.column_stack([X_hours, X_quiz])
y_gauss = np.concatenate([y_g0, y_g1])

X_g_train, X_g_test, y_g_train, y_g_test = train_test_split(
    X_gauss, y_gauss, test_size=0.25, random_state=42, stratify=y_gauss
)

gnb = GaussianNB()
gnb.fit(X_g_train, y_g_train)
y_g_pred = gnb.predict(X_g_test)
y_g_proba = gnb.predict_proba(X_g_test)

g_acc = accuracy_score(y_g_test, y_g_pred)
g_prec = precision_score(y_g_test, y_g_pred)
g_rec = recall_score(y_g_test, y_g_pred)
g_f1 = f1_score(y_g_test, y_g_pred)
g_cm = confusion_matrix(y_g_test, y_g_pred)

print(f"GaussianNB Dataset Shape: {X_gauss.shape}")
print(f"Class Means (theta_):\n  Class 0 (Hours, Quiz): {gnb.theta_[0]}\n  Class 1 (Hours, Quiz): {gnb.theta_[1]}")
print(f"Class Variances (var_):\n  Class 0: {gnb.var_[0]}\n  Class 1: {gnb.var_[1]}")
print(f"GaussianNB Test Metrics:")
print(f"  Accuracy:  {g_acc:.4f} ({g_acc*100:.1f}%)")
print(f"  Precision: {g_prec:.4f} ({g_prec*100:.1f}%)")
print(f"  Recall:    {g_rec:.4f} ({g_rec*100:.1f}%)")
print(f"  F1-Score:  {g_f1:.4f} ({g_f1*100:.1f}%)")
print(f"Confusion Matrix:\n{g_cm}")

print("\nALL VERIFICATIONS COMPLETED SUCCESSFULLY.")
