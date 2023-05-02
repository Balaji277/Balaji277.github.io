import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Generate some random data
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)
y=np.linspace(0,10,len(list(y)))
# Fit logistic regression model
# clf = LogisticRegression(random_state=0).fit(X, y)

# # Plot predicted points
# xx, yy = np.mgrid[-3:3:.01, -3:3:.01]
# grid = np.c_[xx.ravel(), yy.ravel()]
# probs = clf.predict_proba(grid)[:, 1].reshape(xx.shape)
# print("proba: ",clf.predict_proba(grid))
# f, ax = plt.subplots(figsize=(8, 6))
# contour = ax.contourf(xx, yy, probs, 25, cmap="RdBu")
# ax_c = f.colorbar(contour)
# ax_c.set_label("$P(y = 1)$")
# ax_c.set_ticks([0, .25, .5, .75, 1])
plt.scatter(X[:,0], X[:,1], c=y, s=50,
           cmap="RdBu", vmin=-.2, vmax=1.2,
           edgecolor="white", linewidth=1)
# ax.set(aspect="equal",
#        xlim=(-3, 3), ylim=(-3, 3),
#        xlabel="$X_1$", ylabel="$X_2$")
plt.show()
