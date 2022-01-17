FROM pytorch/pytorch

WORKDIR /app/EasyOCR

ENV PIP_NO_CACHE_DIR=true \
    PYTHONDONTWRITEBYTECODE=true

RUN apt-get update -y && \
    apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-dev \
    git \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/li

RUN git clone "https://github.com/JaidedAI/EasyOCR.git" "/app/EasyOCR" \
    && git remote add upstream "https://github.com/JaidedAI/EasyOCR.git" \
    && git pull upstream master

RUN python setup.py build_ext --inplace -j 4 && python -m pip install -e .

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]