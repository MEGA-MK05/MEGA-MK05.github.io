import os

# GitHub 저장소에 이미지를 업로드할 경로 (예: assets/portfolio_slides/)
# 실제 GitHub 경로와 동일하게 맞춰주세요.
IMAGE_BASE_PATH = "/FPGA_multi_asset/emb_img/"
# 이미지 파일 접두사 (예: 슬라이드, slide). '슬라이드' 다음에 숫자가 바로 붙는 경우
IMAGE_PREFIX = "슬라이드" 
# 이미지 파일 확장자 (예: png, jpg)
IMAGE_EXTENSION = "png" 
# 총 슬라이드 개수
NUM_SLIDES = 16 # PPT가 100장이므로 100으로 설정

output_filename = "portfolio_from_ppt.md"

with open(output_filename, "w", encoding="utf-8") as f:
    f.write("# 나의 포트폴리오 (PPT 슬라이드)\n\n")
    f.write("이 포트폴리오는 PPT 슬라이드를 이미지로 변환하여 구성되었습니다.\n\n")
    f.write("---\n\n")

    for i in range(1, NUM_SLIDES + 1):
        # --- 이 부분을 수정해야 합니다! ---
        # 파일명이 '슬라이드0001.png', '슬라이드0002.png' 형태일 경우:
        # i를 4자리 숫자로 포맷하고 앞에 0을 채웁니다.
        image_number_padded = f"{i:04d}" # 예: 1 -> 0001, 10 -> 0010, 100 -> 0100
        image_filename = f"{IMAGE_PREFIX}{image_number_padded}.{IMAGE_EXTENSION}"
        # -----------------------------------

        # GitHub Pages에서 접근할 이미지 전체 경로
        image_full_path = os.path.join(IMAGE_BASE_PATH, image_filename).replace("\\", "/") 

        f.write(f"## 슬라이드 {i}\n")
        f.write(f"![포트폴리오 슬라이드 {i}]({image_full_path})\n\n")
        f.write("---\n\n")

print(f"'{output_filename}' 파일이 성공적으로 생성되었습니다.")
print(f"이미지 경로는 '{IMAGE_BASE_PATH}'로 설정되었습니다. GitHub에 맞게 확인해주세요.")
