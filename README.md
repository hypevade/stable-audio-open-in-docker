# 🎵 Stable Audio Open in Docker

[English](#english) | [Русский](#russian)

---

## 🇺🇸 English

### 🚀 Overview

A Docker container for AI-powered audio generation using **Stable Audio Open 1.0** by Stability AI. This project provides a web interface built with Gradio for creating high-quality audio from text descriptions.

**Repository**: [stabilityai/stable-audio-open-1.0](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### ✨ Features

- 🎼 **AI Audio Generation**: Create audio from text descriptions
- 🚀 **Optimized Performance**: PyTorch optimizations and model compilation
- 🎛️ **Flexible Controls**: Adjustable duration (5-47s), steps (20-200), CFG scale (1-15)
- 🎨 **Rich Examples**: Pre-configured prompts for various audio styles
- 🔧 **Docker Ready**: Easy deployment with Docker and Docker Compose
- 🎯 **GPU Acceleration**: Full NVIDIA GPU support with CUDA

### 🏗️ Architecture

- **Backend**: PyTorch + Stable Audio Tools
- **Frontend**: Gradio web interface
- **Container**: Docker with PyTorch 2.1.2 + CUDA 11.8
- **Model**: Stable Audio Open 1.0 (1.5GB)

### 📋 Requirements

- Docker with NVIDIA GPU support
- NVIDIA Container Toolkit
- Hugging Face API token
- Minimum 8GB GPU VRAM (16GB recommended)

### 🚀 Quick Start

#### 1. Clone Repository
```bash
git clone <your-repo-url>
cd stable-audio-open-in-docker
```

#### 2. Setup Environment
```bash
cp env.example .env
# Edit .env with your HF_TOKEN
```

#### 3. Launch Container
```bash
docker-compose up --build
```

#### 4. Open Browser
Navigate to: http://localhost:8000

### ⚙️ Configuration

#### Environment Variables (.env)
```bash
# Required: Get from https://huggingface.co/settings/tokens
HF_TOKEN=your_huggingface_token_here

# Optional: Hugging Face cache path
HF_CACHE_PATH=/path/to/cache

# Optional: CUDA home directory
CUDA_HOME=/usr/local/cuda

# Optional: Server port
SERVER_PORT=8000
```

#### Generation Parameters
- **Duration**: 5-47 seconds (15s recommended for speed)
- **Steps**: 20-200 diffusion steps (50 recommended for speed)
- **CFG Scale**: 1-15 (7 recommended for balance)

### 🎵 Usage Examples

#### Ambient Music
```
"Deep ambient focus music with rich low-end textures and evolving bass drones. 
Soft atmospheric layers, slow harmonic shifts, subtle sub-bass pulses, analog warmth, 
filtered noise. Inspired by early morning stillness and internal reflection."
```

#### Lo-Fi Beats
```
"A chilled, atmospheric lo-fi beat with warm vinyl crackle, soft piano chords, 
and mellow synth textures. Slow tempo. Dreamy and nostalgic mood."
```

#### Nature Sounds
```
"Recreate a gentle rainfall with distant thunder."
```

#### Studio Recording
```
"Rock beat played in a treated studio, session drumming on an acoustic kit."
```

### 🔧 Technical Details

#### Model Information
- **Base Model**: Stable Audio Open 1.0
- **Sample Rate**: 44.1 kHz
- **Audio Format**: WAV (16-bit)
- **Generation Method**: Diffusion-based text-to-audio

#### Performance Optimizations
- PyTorch 2.1.2 with CUDA 11.8
- Model compilation with `torch.compile`
- Mixed precision (FP16) generation
- DPM++ 3M SDE sampler
- Optimized memory management

#### Audio Processing
- Automatic duration trimming
- Normalization and clipping
- High-quality audio output
- Unique filename generation

### 📁 Project Structure
```
stable-audio-open-in-docker/
├── app/                    # Application directory
├── docker-compose.yaml     # Docker Compose configuration
├── Dockerfile             # Docker image definition
├── main.py                # Main application (Gradio interface)
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
├── .gitignore            # Git exclusions
└── README.md             # This file
```

### 🐛 Troubleshooting

#### Common Issues
1. **CUDA Out of Memory**: Reduce batch size or use shorter audio
2. **Model Loading Slow**: Check internet connection and HF token
3. **Audio Quality Issues**: Increase diffusion steps or CFG scale

#### Performance Tips
- Use 15s duration + 50 steps for fast generation
- Higher steps = better quality but slower generation
- CFG scale 7-9 provides good balance

### 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🇷🇺 Русский

### 🚀 Обзор

Docker контейнер для генерации аудио с помощью ИИ, использующий **Stable Audio Open 1.0** от Stability AI. Этот проект предоставляет веб-интерфейс, построенный на Gradio, для создания высококачественного аудио из текстовых описаний.

**Репозиторий**: [stabilityai/stable-audio-open-1.0](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### ✨ Возможности

- 🎼 **Генерация аудио ИИ**: Создание аудио из текстовых описаний
- 🚀 **Оптимизированная производительность**: Оптимизации PyTorch и компиляция модели
- 🎛️ **Гибкое управление**: Настраиваемая длительность (5-47с), шаги (20-200), CFG масштаб (1-15)
- 🎨 **Богатые примеры**: Предустановленные промпты для различных стилей аудио
- 🔧 **Готов к Docker**: Простое развертывание с Docker и Docker Compose
- 🎯 **GPU ускорение**: Полная поддержка NVIDIA GPU с CUDA

### 🏗️ Архитектура

- **Бэкенд**: PyTorch + Stable Audio Tools
- **Фронтенд**: Веб-интерфейс Gradio
- **Контейнер**: Docker с PyTorch 2.1.2 + CUDA 11.8
- **Модель**: Stable Audio Open 1.0 (1.5 ГБ)

### 📋 Требования

- Docker с поддержкой NVIDIA GPU
- NVIDIA Container Toolkit
- Токен API Hugging Face
- Минимум 8 ГБ GPU VRAM (рекомендуется 16 ГБ)

### 🚀 Быстрый старт

#### 1. Клонирование репозитория
```bash
git clone <url-вашего-репозитория>
cd stable-audio-open-in-docker
```

#### 2. Настройка окружения
```bash
cp env.example .env
# Отредактируйте .env с вашим HF_TOKEN
```

#### 3. Запуск контейнера
```bash
docker-compose up --build
```

#### 4. Открытие браузера
Перейдите по адресу: http://localhost:8000

### ⚙️ Конфигурация

#### Переменные окружения (.env)
```bash
# Обязательно: Получите на https://huggingface.co/settings/tokens
HF_TOKEN=ваш_токен_huggingface

# Опционально: Путь к кэшу Hugging Face
HF_CACHE_PATH=/путь/к/кэшу

# Опционально: Директория CUDA
CUDA_HOME=/usr/local/cuda

# Опционально: Порт сервера
SERVER_PORT=8000
```

#### Параметры генерации
- **Длительность**: 5-47 секунд (15с рекомендуется для скорости)
- **Шаги**: 20-200 шагов диффузии (50 рекомендуется для скорости)
- **CFG масштаб**: 1-15 (7 рекомендуется для баланса)

### 🎵 Примеры использования

#### Эмбиент музыка
```
"Глубокая эмбиент музыка для концентрации с богатыми низкочастотными текстурами 
и развивающимися басовыми дронами. Мягкие атмосферные слои, медленные 
гармонические сдвиги, тонкие пульсации саб-баса, аналоговое тепло, 
фильтрованный шум. Вдохновлено утренней тишиной и внутренней рефлексией."
```

#### Lo-Fi биты
```
"Расслабленный атмосферный lo-fi бит с теплым виниловым потрескиванием, 
мягкими фортепианными аккордами и меланхоличными синтезаторными текстурами. 
Медленный темп. Мечтательное и ностальгическое настроение."
```

#### Звуки природы
```
"Воссоздать нежный дождь с далеким громом."
```

#### Студийная запись
```
"Рок бит, сыгранный в обработанной студии, сессионная игра на барабанах 
акустической установки."
```

### 🔧 Технические детали

#### Информация о модели
- **Базовая модель**: Stable Audio Open 1.0
- **Частота дискретизации**: 44.1 кГц
- **Формат аудио**: WAV (16-бит)
- **Метод генерации**: Диффузионная генерация текст-в-аудио

#### Оптимизации производительности
- PyTorch 2.1.2 с CUDA 11.8
- Компиляция модели с `torch.compile`
- Генерация в смешанной точности (FP16)
- Сэмплер DPM++ 3M SDE
- Оптимизированное управление памятью

#### Обработка аудио
- Автоматическая обрезка по длительности
- Нормализация и ограничение
- Высококачественный аудиовыход
- Генерация уникальных имен файлов

### 📁 Структура проекта
```
stable-audio-open-in-docker/
├── app/                    # Директория приложения
├── docker-compose.yaml     # Конфигурация Docker Compose
├── Dockerfile             # Определение Docker образа
├── main.py                # Основное приложение (интерфейс Gradio)
├── requirements.txt       # Python зависимости
├── env.example           # Шаблон переменных окружения
├── .gitignore            # Исключения Git
└── README.md             # Этот файл
```

### 🐛 Устранение неполадок

#### Частые проблемы
1. **Нехватка памяти CUDA**: Уменьшите размер батча или используйте более короткое аудио
2. **Медленная загрузка модели**: Проверьте интернет-соединение и токен HF
3. **Проблемы качества аудио**: Увеличьте шаги диффузии или CFG масштаб

#### Советы по производительности
- Используйте 15с длительность + 50 шагов для быстрой генерации
- Больше шагов = лучше качество, но медленнее генерация
- CFG масштаб 7-9 обеспечивает хороший баланс

### 📄 Лицензия

MIT License - см. файл [LICENSE](LICENSE) для деталей.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

*Made with ❤️ for the AI audio community*
