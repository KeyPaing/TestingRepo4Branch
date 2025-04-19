import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;

class BubbleSortTest {

    @Test
    void testBubbleSort_emptyArray() {
        int[] arr = {};
        BubbleSort.bubbleSort(arr);
        assertEquals(0, arr.length);
    }

    @Test
    void testBubbleSort_singleElementArray() {
        int[] arr = {5};
        BubbleSort.bubbleSort(arr);
        assertArrayEquals(new int[]{5}, arr);
    }

    @Test
    void testBubbleSort_alreadySortedArray() {
        int[] arr = {1, 2, 3, 4, 5};
        BubbleSort.bubbleSort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, arr);
    }

    @Test
    void testBubbleSort_reverseSortedArray() {
        int[] arr = {5, 4, 3, 2, 1};
        BubbleSort.bubbleSort(arr);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, arr);
    }

    @Test
    void testBubbleSort_unsortedArray() {
        int[] arr = {5, 1, 4, 2, 8};
        BubbleSort.bubbleSort(arr);
        assertArrayEquals(new int[]{1, 2, 4, 5, 8}, arr);
    }

    @Test
    void testBubbleSort_duplicateElements() {
        int[] arr = {5, 1, 4, 2, 8, 1, 5};
        BubbleSort.bubbleSort(arr);
        assertArrayEquals(new int[]{1, 1, 2, 4, 5, 5, 8}, arr);
    }

    @Test
    void testBubbleSort_negativeElements() {
        int[] arr = {-5, 1, -4, 2, -8};
        BubbleSort.bubbleSort(arr);
        assertArrayEquals(new int[]{-8, -5, -4, 1, 2}, arr);

    }

    @Test
    void testBubbleSort_mixedPositiveAndNegativeElements() {
        int[] arr = {-5, 1, -4, 2, -8, 0, 10};
        BubbleSort.bubbleSort(arr);
        assertArrayEquals(new int[]{-8, -5, -4, 0, 1, 2, 10}, arr);
    }


}
