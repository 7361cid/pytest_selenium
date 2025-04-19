import random
import time
import re

from pages.base_page import BasePage
from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizePageLocators,\
    DragPageLocators, DragablePageLocators


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_items(self, element):
        items = self.elements_are_visible(element)
        return [item.text for item in items]

    def shared_steps(self, tab, items):
        self.element_is_visible(tab).click()
        order_before = self.get_items(items)
        item_from, item_to = random.sample(self.elements_are_visible(items), k=2)
        self.action_drag_and_drop_to_element(item_from, item_to)
        order_after = self.get_items(items)
        return order_before, order_after

    def change_list_order(self):
        return self.shared_steps(self.locators.TAB_LIST, self.locators.ITEMS_LIST)

    def change_grid_order(self):
        return self.shared_steps(self.locators.TAB_GRID, self.locators.ITEMS_GRID)


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        items = self.elements_are_visible(elements)
        item = random.sample(items, k=1)
        item[0].click()

    def select_from_list(self):
        self.element_is_visible(locator=self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        return self.element_is_visible(self.locators.LIST_ITEM_ACTIVE).text

    def select_from_grid(self):
        self.element_is_visible(locator=self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        return self.element_is_visible(self.locators.GRID_ITEM).text


class ResizePage(BasePage):
    locators = ResizePageLocators

    def parse_size(self, style):
        width = style.split(";")[0].split(":")[1].replace(" ", "")
        height = style.split(";")[1].split(":")[1].replace(" ", "")
        return width, height

    def get_max_mix_size(self, element):
        element = self.element_is_visible(element)
        size = element.get_attribute('style')
        return self.parse_size(size)

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.locators.RESIZABLE_BOX_HANDLE, 300, 150, True)
        max_size = self.get_max_mix_size(self.locators.RESIZABLE_BOX)
        self.action_drag_and_drop_by_offset(self.locators.RESIZABLE_BOX_HANDLE, -300, -150, True)
        min_size = self.get_max_mix_size(self.locators.RESIZABLE_BOX)
        return max_size, min_size

    def change_size_resizable(self):
        handle = self.element_is_present(self.locators.RESIZABLE_HANDLE)
        self.go_to_element(handle)
        self.action_drag_and_drop_by_offset(self.locators.RESIZABLE_HANDLE, 50, 25, True)
        max_size = self.get_max_mix_size(self.locators.RESIZABLE)
        self.action_drag_and_drop_by_offset(self.locators.RESIZABLE_HANDLE, -100, -50, True)
        min_size = self.get_max_mix_size(self.locators.RESIZABLE)
        return max_size, min_size


class DragPage(BasePage):
    locators = DragPageLocators()

    def drop_simple(self):
        drag = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag, drop)
        return drop.text

    def accept_drop(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_not_accept = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drag_accept = self.element_is_visible(self.locators.ACCEPTABLE)
        drop = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(drag_not_accept, drop)
        text = drop.text
        self.action_drag_and_drop_to_element(drag_accept, drop)
        text2 = drop.text
        return text, text2

    def prevent_propagation_droppable(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner)
        text = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT)
        text2 = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT)
        self.action_drag_and_drop_to_element(drag_div, greedy_inner)
        return text.text, not_greedy_inner.text, text2.text, greedy_inner.text

    def revert_droppable(self, element_name):
        elements = {"will_revert": self.locators.WILL_REVERT, "not_revert": self.locators.NOT_REVERT}
        self.element_is_visible(self.locators.REVERT_TAB).click()
        element = self.element_is_visible(elements[element_name])
        drop = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(element, drop)
        position_after_move = element.get_attribute('style')
        time.sleep(1)
        position_after_revert = element.get_attribute('style')
        return position_after_move, position_after_revert


class DragablePage(BasePage):
    locators = DragablePageLocators()

    elements = {"x": locators.ONLY_X, "y": locators.ONLY_Y}
    def get_positions(self, element):
        before_position = element.get_attribute('style')
        self.action_drag_and_drop_by_offset(element, random.randint(0, 50), random.randint(0, 50))
        after_position = element.get_attribute('style')
        return before_position, after_position

    def drag_simple(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        pos1, pos2 = self.get_positions(drag_div)
        return pos1, pos2

    def get_top_position(self, position):
        if "top" in position:
            numbers = re.findall(r'top: \d+px', position)
            return numbers[0][5:]
        else:
            return "0px"

    def get_left_position(self, position):
        if "left" in position:
            numbers = re.findall(r'left: \d+px', position)
            return numbers[0][6:]
        else:
            return "0px"

    def axis_restricted(self, axis):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        drag_element = self.element_is_visible(self.elements[axis])
        positions = self.get_positions(drag_element)
        top_position_before = self.get_top_position(positions[0])
        top_position_after = self.get_top_position(positions[1])
        left_position_before = self.get_left_position(positions[0])
        left_position_after = self.get_left_position(positions[1])
        return left_position_before, left_position_after, top_position_before, top_position_after



