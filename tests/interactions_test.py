import time

from pages.interactions_page import SortablePage, SelectablePage, ResizePage, DragPage, DragablePage


class TestInteractions:
    # class TestSortablePage:
    #     def test_sort_list(self, driver):
    #         page = SortablePage(driver, "https://demoqa.com/sortable")
    #         page.open()
    #         before, after = page.change_list_order()
    #         assert before != after
    #
    #     def test_sort_grid(self, driver):
    #         page = SortablePage(driver, "https://demoqa.com/sortable")
    #         page.open()
    #         before, after = page.change_grid_order()
    #         assert before != after

    # class TestSelectablePage:
    #     def test_select_from_list(self, driver):
    #         page = SelectablePage(driver, "https://demoqa.com/selectable")
    #         page.open()
    #         text = page.select_from_list()
    #         text2 = page.select_from_grid()
    #         assert text != ''
    #         assert text2 != ''

    # class TestResizePage:
    #     def test_resize(self, driver):
    #         page = ResizePage(driver, "https://demoqa.com/resizable")
    #         page.open()
    #         size = page.change_size_resizable_box()
    #         size2 = page.change_size_resizable()
    #         assert size[0] != size[1]
    #         assert size2[0] != size2[1]

   # class TestDragPage:
        # def test_simple_drag(self, driver):
        #     page = DragPage(driver, "https://demoqa.com/droppable")
        #     page.open()
        #     text = page.drop_simple()
        #     assert text == "Dropped!"

        # def test_accept_droppable(self, driver):
        #     page = DragPage(driver, "https://demoqa.com/droppable")
        #     page.open()
        #     text, text2 = page.accept_drop()
        #     assert text == "Drop here"
        #     assert text2 == "Dropped!"

        # def test_prevent_propagation_droppable(self, driver):
        #     page = DragPage(driver, "https://demoqa.com/droppable")
        #     page.open()
        #     text, text2, text3, text4 = page.prevent_propagation_droppable()
        #     assert text == "Dropped!"
        #     assert text2 == "Dropped!"
        #     assert text3 == "Outer droppable"
        #     assert text4 == "Dropped!"

        # def test_revert_droppable(self, driver):
        #     page = DragPage(driver, "https://demoqa.com/droppable")
        #     page.open()
        #     pos1, pos2 = page.revert_droppable("will_revert")
        #     assert pos1 != pos2
        #     pos1, pos2 = page.revert_droppable("not_revert")
        #     assert pos1 == pos2

    class TestDragablePage:
        # def test_dragable_simlpe(self, driver):
        #     page = DragablePage(driver, "https://demoqa.com/dragabble")
        #     page.open()
        #     pos1, pos2 = page.drag_simple()
        #     assert pos1 != pos2

        def test_axis_restricted(self, driver):
            page = DragablePage(driver, "https://demoqa.com/dragabble")
            page.open()
            x1, x2, y1, y2 = page.axis_restricted("x")
            assert x1 != x2
            assert y1 == y2
            x1, x2, y1, y2 = page.axis_restricted("y")
            assert x1 == x2
            assert y1 != y2