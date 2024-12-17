<h1 align=center><font size = 5>Building Software to Calculate Legendre Differential Equations</font></h1>

<img  src="https://raw.githubusercontent.com/doguilmak/Legendre-Differential-Equations-Calculator-Software/refs/heads/main/assets/spherical_harmonics.png"  alt="Potential Theory and Static Gravity Field of the Earth">

<small>Picture Source: <a  href="https://ui.adsabs.harvard.edu/abs/2007gdsy.book...11J/abstract">Potential Theory and Static Gravity Field of the Earth</a></small>

<br>

## Statement

The aim of this project, as indicated by the title, is to develop an application that can calculate *Legendre differential equations* using Python 3.7 and save the results in an *Excel spreadsheet*. The application was built using the *PyQt5* library along with the *Qt Designer* tool for the graphical interface. You can find various versions of the program in the project repository, including those with and without graphical outputs.

<br>

## Methodology

### Unnormalized Legendre Function

The **unnormalized Legendre function** is a solution to the Legendre differential equation, which is commonly used in problems involving spherical symmetry, such as gravitational and electrostatic potentials. The unnormalized Legendre function is expressed as:

$$P_{nm}(t) = 2^{-m} \cdot (1 - t^{2})^{\frac{m}{2}} \cdot \sum_{k=0}^{r} (-1)^{k} \cdot \frac{(2n - 2k)! \cdot t^{n - m - 2k}}{k! (n - k)! (n - m - 2k)!}$$

Where:
- $t$ is the variable, typically the cosine of the polar angle $\theta$ in spherical coordinates.
- $n$ is the degree, and $m$ is the order of the polynomial, both of which are non-negative integers satisfying $0 \leq m \leq n$.
- The summation term is the series expansion used to compute the Legendre polynomial for given values of $n$, $m$, and $t$. The term $r$ determines the truncation of the series, often based on the desired precision.
- The factor $2^{-m}$ and $(1 - t^{2})^{\frac{m}{2}}$ are scaling factors that simplify the computation of the Legendre polynomials.

This equation provides the raw solution to the Legendre differential equation without any additional normalization. It is useful for understanding the basic structure of the Legendre polynomials.

<br>

### Normalized Legendre Function

The **normalized Legendre function** is derived from the unnormalized version, but it includes a normalization factor that ensures the Legendre polynomials are orthonormal. This is especially important in applications where the polynomials are used as part of a basis for function expansion, such as in quantum mechanics or geodesy. The normalized Legendre function is expressed as:

$$P_{nm}(t) = 2^{-m} \cdot (1 - t^{2})^{\frac{m}{2}} \cdot \sum_{k=0}^{r} (-1)^{k} \cdot \frac{(2n - 2k)! \cdot t^{n - m - 2k}}{k! (n - k)! (n - m - 2k)!} \cdot \sqrt{\frac{2^{2(n + 1)} \cdot (n - m)!}{(n + m)!}}$$

Where:
- The first part of the equation is identical to the unnormalized version, including the summation term, $t$-dependent factors, and scaling terms.
- The **normalization factor** is given by:

$$\sqrt{\frac{2^{2(n + 1)} \cdot (n - m)!}{(n + m)!}}$$

This factor adjusts the Legendre function so that it becomes **orthonormal**, meaning that it satisfies the following integral condition:

$$\int_{-1}^{1} P_{nm}(t) \cdot P_{n'm'}(t) \, dt = \delta_{nn'} \delta_{mm'}$$

Where $\delta$ is the Kronecker delta function, which is equal to 1 if the indices are the same, and 0 otherwise.

The normalization is crucial in many applications, such as:
- In solving Laplace's equation in spherical coordinates.
- In expanding spherical functions into series of spherical harmonics in quantum mechanics.
- In geodesy and astronomy, where the Legendre polynomials are used for approximating functions on a sphere.

The normalization ensures that the polynomials are properly scaled for these types of analyses, where orthogonality is a key property.

<br>

**Normalized Legendre Function**: This function includes a **normalization factor** that ensures orthogonality over the interval $[-1, 1]$. It is particularly useful in fields like  **geodesy**, and **astrophysics**, where spherical harmonics and orthonormal bases are required.

For this project, the focus is on computing the **normalized Legendre function**, and these values are stored in an **Excel file** for further analysis and visualization. The unnormalized function provides the foundation for the normalized form but is not directly used in the computations here.

<br>

<h2>UI Overview:</h2>

<div align="center">
	<img width=600  height=750 src="UI.jpg">
</div>

<br>

<h2>Analysis</h2>

You can examine the excel output, where $n$ and $m$> values ​​are $10$, on the *output.xlsx* file. The same output is also shown in the application interface. In order for it to be saved as Excel as optional, it must first be written in the relevant field, indicating the name of the file. (for example: '<i>C:\Users\User\Desktop\output.xlsx</i>')

<br>

## File Conversions

**Before proceeding with these operations, you must navigate to the directory where the _Calculating_Pnm_excel.ui_ and _Calculating_Pnm_excel.py_ files are stored using the command prompt.**

These procedures were set up by me, but you are welcome to create a `.exe` file from the `.py` script. If you're interested in learning how to do this or want to explore the process further, feel free to follow the instructions provided in this section.

### .ui to .py

    python -m PyQt5.uic.pyuic -x Calculating_Pnm_excel.ui -o Calculating_Pnm_excel.py

<br>

### .py to .exe

    pyinstaller.exe --onefile --windowed --icon=app.ico Calculating_Pnm_excel.py

<br>

## Reference

Jekeli, C. (2007). Potential theory and static gravity field of the Earth. _Geodesy_, _3_, 11-42.
