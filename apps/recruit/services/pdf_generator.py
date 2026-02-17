from pathlib import Path


class PDFGeneratorService:
    """MVP placeholder service for PDF generation."""

    def generate(self, cv_id: int, language: str = "fr") -> Path:
        output_path = Path("media/generated")
        output_path.mkdir(parents=True, exist_ok=True)
        file_path = output_path / f"cv_{cv_id}_{language}.pdf"
        # Placeholder content; replace with real PDF rendering library later.
        file_path.write_bytes(b"%PDF-1.4\n% Mboko Recruit placeholder PDF\n")
        return file_path
