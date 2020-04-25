from word2number import w2n

class OrderSheet():
    def product_count(self,cell_value):
        # converters = ['count_yes', 'count_word']
        # for f in converters:
            # return getattr(self, f,)
        try:
            if cell_value.lower() == 'yes':
                return 1
        except Exception as e:
            return cell_value

    # def count_yes(self, cell_value):