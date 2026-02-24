import os
import base64
from typing import Dict, Any
from pathlib import Path


class LogoService:
    LOGO_MAP = {
        "RAKINSURANCE": "rak.png",
        "GIG": "gig.png",
        "AIG": "aig.png",
    }

    def __init__(self):
        # Resolve project root safely
        self.base_dir = Path(__file__).resolve().parents[2] / "static" / "logos"

    def _encode_logo(self, file_path: str) -> str:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string

    def attach_logos(self, context: Dict[str, Any]) -> Dict[str, Any]:
        updated_context = context.copy()

        quotes = updated_context.get("quotes", [])

        for quote in quotes:
            insurer_name = quote.get("insurer", {}).get("name")
            logo_file = self.LOGO_MAP.get(insurer_name)

            if logo_file:
                file_path = os.path.join(self.base_dir, logo_file)

                if os.path.exists(file_path):
                    quote["logo_base64"] = self._encode_logo(file_path)
                else:
                    print("Logo file not found:", file_path)
                    quote["logo_base64"] = None
            else:
                quote["logo_base64"] = None

        return updated_context