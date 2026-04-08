from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/image/{character_name}")
async def get_character_ranking(character_name: str):
    try:
        response = requests.get(
            f"https://www.nexon.com/api/maplestory/no-auth/ranking/v2/na?type=overall&id=weekly&reboot_index=0&page_index=1&character_name={character_name}"
        )
        data = response.json()

        if data.get("ranks"):
            character = data["ranks"][0]
            return {
                "name": character["characterName"],
                "image_url": character["characterImgURL"]
            }
        else:
            return {
                "error": "Could not find character"
            }
    except:
        return {
            "error": "Error occured"
        }