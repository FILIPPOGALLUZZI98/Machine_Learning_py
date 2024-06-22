# Algoritmo per calcolare la cost function regolarizzata
def cost_function(X, y, w, b, lambda_):
    m = X.shape[0]
    n = len(w)
    cost = 0.
    for i in range(m):
        f_wb_i = np.dot(X[i], w) + b
        cost = cost + (f_wb_i - y[i])**2
    cost = cost / (2 * m)
    reg_cost = 0
    for j in range(n):
        reg_cost += (w[j]**2)
    reg_cost = (lambda_/(2*m)) * reg_cost
    total_cost = cost + reg_cost
    return total_cost

# Algoritmo per calcolare il gradiente regolarizzato
def gradient(X, y, w, b, lambda_):
    m, n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.
    for i in range(m):
        err = (np.dot(X[i], w) + b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * X[i, j]
        dj_db = dj_db + err
    dj_dw = dj_dw / m
    dj_db = dj_db / m
    for j in range(n):
        dj_dw[j] = dj_dw[j] + (lambda_/m) * w[j]
    return dj_db, dj_dw

# Funzione per il gradiente discendente
def gradient_descent(X, y, w_in, b_in, alpha, num_iters, lambda_):
    J_history = []
    w = copy.deepcopy(w_in)
    b = b_in
    for i in range(num_iters):
        dj_db, dj_dw = gradient(X, y, w, b, lambda_)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        if i < 100000: 
            J_history.append(cost_function(X, y, w, b, lambda_))
        # Stampa il costo a intervalli di 10 volte o per il numero di iterazioni se < 10
        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]}")
    return w, b, J_history 




# Facciamo i grafici per 4 valori di alpha (con lambda=0) e con 4 valori di lambda con il migliore alpha
initial_w = np.zeros(X.shape[1]); initial_b = 0.; iterations = 10000

alpha_values = [1e-7, 1e-6, 1e-5, 1e-4]
plt.figure(figsize=(14, 10))
for i, alpha in enumerate(alpha_values):
    _,_,J_history = gradient_descent(X, y, initial_w, initial_b, alpha=alpha, num_iters=iterations, lambda_=0)
    plt.subplot(2, 2, i + 1)
    plt.plot(J_history); plt.title(f'Alpha = {alpha}'); plt.xlabel('Iterations'); plt.ylabel('Cost J')
plt.tight_layout(); plt.show()

lambda_values = [0.05, 0.1, 0.5, 1]
plt.figure(figsize=(14, 10))
for i, lambda_ in enumerate(lambda_values):
    _,_,J_history = gradient_descent(X, y, initial_w, initial_b, alpha=1e-5, num_iters=iterations, lambda_=lambda_)
    plt.subplot(2, 2, i + 1); plt.plot(J_history); plt.title(f'Lambda = {lambda_}'); plt.xlabel('Iterations'); plt.ylabel('Cost J')
plt.tight_layout(); plt.show()


# Facciamo ora il gradient descent con i migliori valori di alpha e lambda
initial_w = np.zeros(X.shape[1]); initial_b = 0.; iterations = 1000000; alpha = 1.0e-5; lambda_ = 0
w_final, b_final, _ = gradient_descent(X, y, initial_w, initial_b, alpha, iterations, lambda_)