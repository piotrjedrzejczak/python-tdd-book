from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User tries to add an empty list item by hitting enter on the home page.

        # Page refreshes, and there is an error message saying
        # that you cannot add empty list items.

        # User tries again, which now works.

        # User tries to add a second blank list item.

        # Receives a simmilar warning message from the webpage.

        # She can correct it by filling some text in.
        self.fail('finish the test buddy')
