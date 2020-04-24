import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
#大型项目时，常需要在添加新代码前重构既有代码，旨在简化既有代码结构，使得更容易拓展。该项目以此模块存储大量让游戏运行的函数。以使得主函数更容易理解
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
      fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
    """alien's rows in the screen"""
    available_space_y = ai_settings.screen_height - 3 * alien_height-ship_height
    number_rows = int (available_space_y/(2*alien_height))
    return  number_rows

def get_number_aliens_x(ai_settings,alien_width):
    """aliens' numbers in each line"""
    # 创建一个外星人，并计算一行可容纳多少
    # 外星人间距为外星人宽度
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x/(2 * alien_width))
    return number_aliens_x
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """create one alien and put it in the line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height*row_number
    aliens.add(alien)
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """响应按键与鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果点叉叉，即退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """每次进行操作更换新图像，切换到新屏幕"""
    # 绘制屏幕颜色
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后重新绘制所有子弹
    for bullet in bullets.sprites():
            bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #显示得分
    sb.show_score()
    # 若游戏处于非活动状态
    if not stats.game_active:
        play_button.draw_button()
    # 让最近的绘制屏幕可见
    pygame.display.flip()  # 即每次while循环，擦去旧界面，绘制新界面


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹位置，并删除已经消失的子弹"""
    #更新子弹的位置
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets)
        check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """update the bullet and delete"""
    # check the knock between bullet and aliens
    # if ture, delete the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)

        sb.prep_score()
    if len(aliens) == 0:
        #delete bullets and create aliens
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        #等级增加
        stats.level += 1
        sb.prep_level()
        ai_settings.increase_speed()

def update_aliens(ai_settings,stats,sb,ship,aliens,bullets,screen):
    """check and update aliens"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #check collisions between ship and aliens
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings, stats,sb, screen, ship, aliens, bullets)
def check_fleet_edges(ai_settings,aliens):
    """the measure once the alien reach the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """下移"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """response the ship which was crashed"""
    if stats.ships_left > 0:
        # ships_left-1
        stats.ships_left -= 1
        #更新计分板
        sb.prep_ships()
        # 清空aliens and bullets
        aliens.empty()
        bullets.empty()
        # restart
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # stop
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """check if there are any alien reach the bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """touch the button to start game"""
    button_clicked =play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        #清空外星人与子弹列表

        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
def check_high_score(stats,sb):
    if stats.score >stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()