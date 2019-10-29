import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

fig, ax = plt.subplots(1, 3, figsize=(10, 4))
singular_values = []
for i, img_name in enumerate(["../board.png", "../jellyfish.jpg", "../new-york.jpg"]):
    img = Image.open(f"{img_name:s}").convert("L")
    img = np.array(img)
    ax[i].imshow(img, cmap="gray")
    ax[i].axis("off")
    
    U, D, V = np.linalg.svd(img)
    singular_values.append(D)

plt.tight_layout()
plt.savefig(f"../figs/original_img.png", bbox_layout="tight")
plt.clf()



N_list = 2**np.arange(1, 10)
M = len(N_list)
comp_ratio = np.zeros((M,3))
for j in range(M):
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))
    N = N_list[j]
    for i, img_name in enumerate(["../board.png", "../jellyfish.jpg", "../new-york.jpg"]):
        img = Image.open(f"{img_name:s}").convert("L")
        img = np.array(img)

        U, D, V = np.linalg.svd(img)
        D = np.diag(D)

        U2 = U[:, :N]
        D2 = D[:N, :N]
        V2 = V[:N, :]
        img2 = U2@D2@V2
        
        comp_ratio[j, i] = (img.shape[0]*img.shape[1])/(2*N**2 + N)

        ax[i].imshow(img2, cmap="gray")
        ax[i].axis("off")
        ax[i].set_title(f"r = {N}, Comp Ratio = {comp_ratio[j, i]:.1f}")
    plt.tight_layout()
    plt.savefig(f"../figs/img{j}.png", bbox_layout="tight")
    plt.clf()
    
for i in range(3):
    plt.semilogy(singular_values[i])
plt.tight_layout()
plt.savefig(f"../figs/singular_values.png", bbox_layout="tight")

plt.plot()