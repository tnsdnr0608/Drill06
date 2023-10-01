from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running, x, y, target_x, target_y, click_hand
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            target_x, target_y = event.x, TUK_HEIGHT - event.y
            click_hand = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
target_x, target_y = x, y
click_hand = False
move_speed = 2  # 캐릭터 이동 속도

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if click_hand:
        hand.draw(target_x, target_y)

    dir_x = target_x - x
    dir_y = target_y - y
    distance = math.sqrt(dir_x ** 2 + dir_y ** 2)

    if distance > 0:
        move = move_speed / distance
        x += dir_x * move
        y += dir_y * move
    else:
        if click_hand:
            click_hand = False
            target_x, target_y = x, y

    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)  # 캐릭터를 현재 위치에 그립니다.
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()