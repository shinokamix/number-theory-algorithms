import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Глава 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. Тестирование чисел на простоту. Проверка заданного числа на простоту. Алгоритм «Решето Эратосфена» (найти все простые числа до n).
    """)
    return


@app.function
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


@app.function
def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    # Создаем список, где каждый индекс = число
    # Изначально считаем все числа простыми
    prime = [True] * (n + 1)

    # 0 и 1 не являются простыми
    prime[0] = False
    prime[1] = False

    # Проходим только до квадратного корня из n
    for i in range(2, int(n ** 0.5) + 1):

        # Если число еще не вычеркнуто,
        # значит оно простое
        if prime[i]:

            # Вычеркиваем все кратные числа
            # Начинаем с i * i
            for j in range(i * i, n + 1, i):
                prime[j] = False

    # Собираем все оставшиеся простые числа
    result = []

    for i in range(2, n + 1):
        if prime[i]:
            result.append(i)

    return result


@app.cell
def _():
    sieve_of_eratosthenes(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.  Разложение числа на простые множители (факторизация).
    """)
    return


@app.function
def factorize(n):
    # Список для хранения простых множителей
    factors = []

    # Начинаем с самого маленького простого числа
    divisor = 2

    # Пока квадрат делителя не превышает число
    while divisor * divisor <= n:

        # Пока число делится без остатка
        while n % divisor == 0:
            # Добавляем делитель в список
            factors.append(divisor)

            # Делим число на найденный множитель
            n //= divisor

        # Переходим к следующему числу
        divisor += 1

    # Если после деления осталось число больше 1,
    # оно тоже является простым множителем
    if n > 1:
        factors.append(n)

    return factors


@app.cell
def _():
    factorize(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Алгоритм Евклида и расширенный алгоритм Евклида (нахождение НОД). Нахождение НОК (выразить через НОД).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Основная идея алгоритма Евклида

    $$
    \gcd(a, b) = \gcd(b, a \bmod b)
    $$
    """)
    return


@app.function
def gcd(a, b):
    # Повторяем, пока второе число не станет равно 0
    while b != 0:
        # Заменяем числа:
        # a становится b,
        # b становится остатком от деления a на b
        a, b = b, a % b

    # Когда b = 0, в a находится НОД
    return a


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Линейное представление НОД

    $$
    a \cdot x + b \cdot y = \gcd(a, b)
    $$
    """)
    return


@app.function
def extended_gcd(a, b):
    # Базовый случай:
    # если b = 0, то НОД = a
    # коэффициенты: x = 1, y = 0
    if b == 0:
        return a, 1, 0

    # Рекурсивно вызываем функцию для (b, a % b)
    gcd, x1, y1 = extended_gcd(b, a % b)

    # Восстанавливаем коэффициенты для текущего шага
    x = y1
    y = x1 - (a // b) * y1

    # Возвращаем НОД и коэффициенты x, y
    return gcd, x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### НОК через НОД

    $$
    \operatorname{lcm}(a,b)=\frac{|a \cdot b|}{\gcd(a,b)}
    $$
    """)
    return


@app.function
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. Операции по модулю (mod n). Быстрое возведение в степень.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Идея быстрого алгоритма

    Быстрое возведение в степень основано на разбиении степени пополам.

    #### Если степень чётная

    $$
    a^n = (a^{n/2})^2
    $$

    ---

    #### Если степень нечётная

    $$
    a^n = a \cdot a^{n-1}
    $$
    """)
    return


@app.function
def fast_power_mod(a, n, mod):
    # Начальное значение результата
    result = 1

    # Сразу уменьшаем число по модулю
    a %= mod

    while n > 0:

        # Если степень нечетная
        if n % 2 == 1:
            result = (result * a) % mod

        # Возводим в квадрат по модулю
        a = (a * a) % mod

        # Делим степень пополам
        n //= 2

    return result


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 5. Нахождение решения системы линейных сравнений.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### **Основная идея решения**

    Дано линейное сравнение:

    $$
    ax \equiv b \pmod m
    $$

    #### Шаг 1. Проверяем существование решения

    Сначала находим:

    $$
    g = \gcd(a,m)
    $$

    Решение существует только тогда, когда:

    $$
    g \mid b
    $$

    то есть НОД числа $a$ и модуля $m$ делит $b$.

    ---

    #### Шаг 2. Используем расширенный алгоритм Евклида

    Находим коэффициент $p$ из равенства:

    $$
    ap + mq = \gcd(a,m)
    $$

    ---

    #### Шаг 3. Находим решение

    Тогда решение вычисляется по формуле:

    $$
    x \equiv p \cdot \frac{b}{g} \pmod{\frac{m}{g}}
    $$
    """)
    return


@app.function
def solve_linear_congruence(a, b, m):
    """
    Решает сравнение: ax ≡ b (mod m)
    Возвращает решение x или None, если решений нет
    """
    # приводим числа по модулю
    a = a % m
    b = b % m

    # находим НОД и коэффициент из расширенного Евклида
    g, p, _ = extended_gcd(a, m)

    # проверяем существование решения
    if b % g != 0:
        return None

    # находим решение
    x = (p * (b // g)) % (m // g)

    return x


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6. Вычисление значения функции Эйлера для заданного n.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Определение
    **Функция Эйлера** $\varphi(n)$ — количество натуральных чисел $k$, таких что:
    $$1 \le k \le n \quad \text{и} \quad \gcd(k, n) = 1$$

    ---

    #### Формула вычисления
    Пусть каноническое разложение $n$ на простые множители:
    $$n = p_1^{\alpha_1} p_2^{\alpha_2} \dots p_m^{\alpha_m}$$
    Тогда:
    $$\varphi(n) = n \cdot \prod_{i=1}^{m} \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^{m} p_i^{\alpha_i - 1}(p_i - 1)$$

    ---

    #### Оценка сложности
    | Параметр | Значение |
    |----------|----------|
    | **Время** | $O(\sqrt{n})$ |
    | **Память** | $O(1)$ |
    """)
    return


@app.function
def euler_phi(n: int) -> int:
    if n <= 0:
        return 0 # n должно быть > 0
    if n == 1:
        return 1

    result = n
    p = 2

    # Перебираем все возможные простые делители до √n
    while p * p <= n:
        if n % p == 0:
            # p — простой делитель, убираем его все степени из n
            while n % p == 0:
                n //= p
            # Применяем формулу: result *= (1 - 1/p)
            result = result * (p - 1) // p
        p += 1

    # Если после цикла n > 1, значит остался один простой делитель > √n
    if n > 1:
        result = result * (n - 1) // n

    return result


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 7. Вычисление остатка от деления a в большой степени на n при помощи теоремы Эйлера.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Теорема Эйлера

    Если $\gcd(a, n) = 1$, то:

    $$
    a^{\varphi(n)} \equiv 1 \pmod{n}
    $$

    Отсюда следует, что показатель можно редуцировать:

    $$
    a^b \equiv a^{b \bmod \varphi(n)} \pmod{n}
    $$

    Это позволяет вычислять $a^b \bmod n$ даже при огромном $b$ — достаточно заменить его на $b \bmod \varphi(n)$.

    ---

    #### Алгоритм

    1. Если $\gcd(a, n) = 1$ — вычисляем $\varphi(n)$ и редуцируем $b \leftarrow b \bmod \varphi(n)$
    2. Вычисляем $a^b \bmod n$ через быстрое возведение в степень

    ---

    #### Оценка сложности
    | Параметр | Значение |
    |----------|----------|
    | **Время** | $O(\sqrt{n} + \log b)$ |
    | **Память** | $O(1)$ |
    """)
    return


@app.function
def euler_pow_mod(a: int, b: int, n: int) -> int:
    if n == 1:
        return 0

    if gcd(a, n) == 1:
        phi = euler_phi(n)
        b = b % phi

    return fast_power_mod(a, b, n)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 8. Вычисление мультипликативного обратного по mod n.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Определение

    Число $a^{-1}$ называется **мультипликативным обратным** к $a$ по модулю $n$, если:

    $$
    a \cdot a^{-1} \equiv 1 \pmod{n}
    $$

    Обратный элемент **существует тогда и только тогда**, когда:

    $$
    \gcd(a, n) = 1
    $$

    то есть $a$ и $n$ взаимно просты.

    ---

    #### Метод 1 (Расширенный алгоритм Евклида)

    Находим $x, y$ такие что:

    $$
    a \cdot x + n \cdot y = \gcd(a, n)
    $$

    Если $\gcd(a, n) = 1$, то $a \cdot x \equiv 1 \pmod{n}$, следовательно $x$ — искомый обратный.

    Берём $x \bmod n$, чтобы получить положительное значение в диапазоне $[0, n)$.

    ---

    #### Метод 2 (Теорема Эйлера)

    По теореме Эйлера:

    $$
    a^{\varphi(n)} \equiv 1 \pmod{n}
    $$

    Откуда:

    $$
    a^{-1} \equiv a^{\varphi(n)-1} \pmod{n}
    $$

    ---

    #### Оценка сложности
    | Метод | Время | Память |
    |-------|-------|--------|
    | Расширенный Евклид | $O(\log \min(a,n))$ | $O(1)$ |
    | Через теорему Эйлера | $O(\sqrt{n} + \log n)$ | $O(1)$ |
    """)
    return


@app.function
def mod_inverse(a, n):
    a = a % n
    g, x, _ = extended_gcd(a, n)

    if g != 1:
        return None

    return x % n


@app.function
def mod_inverse_euler(a, n):
    a = a % n

    if gcd(a, n) != 1:
        return None

    phi = euler_phi(n)
    return fast_power_mod(a, phi - 1, n)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 9. Китайская теорема об остатках.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Постановка задачи

    Дана система сравнений:

    $$
    \begin{cases}
    x \equiv r_1 \pmod{m_1} \\
    x \equiv r_2 \pmod{m_2} \\
    \vdots \\
    x \equiv r_k \pmod{m_k}
    \end{cases}
    $$

    где $m_1, m_2, \ldots, m_k$ — **попарно взаимно простые** модули ($\gcd(m_i, m_j) = 1$ при $i \neq j$).

    ---

    #### Теорема

    При выполнении условия взаимной простоты система имеет **единственное решение** по модулю:

    $$
    M = m_1 \cdot m_2 \cdots m_k
    $$

    ---

    #### Алгоритм построения решения

    **Шаг 1.** Произведение всех модулей:

    $$
    M = \prod_{i=1}^{k} m_i
    $$

    **Шаг 2.** Для каждого $i$ — «частичное произведение»:

    $$
    M_i = \frac{M}{m_i}
    $$

    **Шаг 3.** Для каждого $i$ — обратный к $M_i$ по модулю $m_i$ (расширенный Евклид):

    $$
    y_i \equiv M_i^{-1} \pmod{m_i} \quad \Longleftrightarrow \quad M_i \cdot y_i \equiv 1 \pmod{m_i}
    $$

    **Шаг 4.** Ответ:

    $$
    x \equiv \sum_{i=1}^{k} r_i \cdot M_i \cdot y_i \pmod{M}
    $$

    ---

    #### Оценка сложности
    | Параметр | Значение |
    |----------|----------|
    | **Время** | $O(k \cdot \log M)$ |
    | **Память** | $O(1)$ |
    """)
    return


@app.function
def crt(remainders, moduli):
    k = len(moduli)

    # Проверяем попарную взаимную простоту модулей
    for i in range(k):
        for j in range(i + 1, k):
            if gcd(moduli[i], moduli[j]) != 1:
                return None

    # Шаг 1: M = m₁ · m₂ · ... · mₖ
    M = 1
    for i in range(k):
        M *= moduli[i]

    # Шаги 2–4: для каждого i накапливаем слагаемое rᵢ · Mᵢ · yᵢ
    x = 0
    for i in range(k):
        ri = remainders[i]
        mi = moduli[i]

        # Шаг 2: частичное произведение Mᵢ = M / mᵢ
        Mi = M // mi

        # Шаг 3: обратный элемент yᵢ ≡ Mᵢ⁻¹ (mod mᵢ)
        _, yi, _ = extended_gcd(Mi, mi)
        yi = yi % mi

        # Шаг 4: добавляем слагаемое
        x += ri * Mi * yi

    return x % M


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Глава 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. Деление полиномов над целостным кольцом.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Вычисления в простых конечных полях (произведение и возведение в степень через битовые операции).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Построить поле GF(256).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. Нахождение неприводимых полиномов в конечном поле.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 5. Решение алгебраических уравнений второй степени в конечных полях.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6. Вычисление дискретных логарифмов в конечных полях.
    """)
    return


if __name__ == "__main__":
    app.run()
