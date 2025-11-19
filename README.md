# AI PR Review Agent

An automated Pull Request review agent powered by Multi-Agent AI (Gemini 2.5).

## Features
- **Logic Review**: Analyzes code logic and correctness.
- **Security Review**: Identifies potential security vulnerabilities.
- **Performance Review**: Suggests performance optimizations.
- **Synthesized Feedback**: Combines all insights into a clear, actionable review.

## Setup

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. **Environment Variables**:
   Create a `.env` file in `backend/` with:
   ```
   GOOGLE_API_KEY=your_gemini_api_key
   GITHUB_TOKEN=your_github_token
   ```

## Usage

1. **Start the backend**:
   ```bash
   cd backend
   python -m app.main
   ```
2. **Open the App**:
   Navigate to `http://localhost:8000` in your browser.
3. **Generate Review**:
   Enter the repository name (e.g., `owner/repo`) and PR number to get a review.

