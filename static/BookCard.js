const BookCard = {
  name: 'BookCard',
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  template: `
    <div class="book-card">
      <img :src="book.image" alt="Book cover image" />
      <h2>{{ book.title }}</h2>
      <p>{{ book.author }}</p>
      <p>{{ book.description }}</p>
    </div>
  `
}

export default BookCard