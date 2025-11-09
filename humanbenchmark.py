import pyautogui
import time
#visit the website https://humanbenchmark.com/ to test the scripts. Select the actual game in the website. Select the corresponding one here and switch back to the website (qucikly would be preferable).
game = input("Select game: ")
if game.lower() == "reaction test":
    target_color = (75, 219, 106)
    check_position = (1287, 454)

    print("Waiting for green to appear")

    while True:
        if pyautogui.pixel(*check_position) == target_color:
            pyautogui.click(check_position)
            print("Clicked!")




if game.lower() == "sequence memory":
    time.sleep(2)
    target_colour = (255, 255, 255)

    box_labels = {
        (819, 291): "upper left",
        (954, 291): "upper middle",
        (1079, 291): "upper right",
        (819, 425): "middle left",
        (954, 425): "middle middle",
        (1079, 425): "middle right",
        (819, 556): "lower left",
        (954, 556): "lower middle",
        (1079, 556): "lower right"
    }

    box_coordinates = list(box_labels.keys())

    round = 0
    pyautogui.click(948, 527)
    time.sleep(0.3)

    while True:
        round += 1
        answers = []
        boxes_found = 0
        used_cordinates = None

        print(f"\n[Round {round}] Watching for {round} white flashes...")

        while boxes_found < round:
            for coordinates in box_coordinates:
                pixel = pyautogui.pixel(*coordinates)
                if pixel == target_colour and used_cordinates != coordinates:
                    label = box_labels[coordinates]
                    print(f"Detected: {label}")
                    answers.append(coordinates)
                    boxes_found += 1
                    used_cordinates = coordinates

        time.sleep(0.5)

        print("Clicking in order:")
        for coord in answers:
            label = box_labels[coord]
            print(f"Clicked: {label}")
            pyautogui.click(coord)




if game.lower() == "aim trainer":
    top_left = (529, 209)
    bottom_right = (1377, 629)
    target_color = (149, 195, 232)
    STEP = 3

    max_targets = 32
    clicks_done = 0

    print(f"Waiting to click {max_targets} targets...")

    while clicks_done < max_targets:
        screen = pyautogui.screenshot(region=(
            top_left[0],
            top_left[1],
            bottom_right[0] - top_left[0],
            bottom_right[1] - top_left[1]
        ))

        found = False
        for x in range(0, bottom_right[0] - top_left[0], STEP):
            for y in range(0, bottom_right[1] - top_left[1], STEP):
                pixel = screen.getpixel((x, y))
                if pixel == target_color:
                    abs_x = top_left[0] + x
                    abs_y = top_left[1] + y
                    pyautogui.click(abs_x, abs_y)
                    clicks_done += 1
                    print(f"[{clicks_done}] Clicked at: ({abs_x}, {abs_y})")
                    found = True
                    break
            if found:
                break


















