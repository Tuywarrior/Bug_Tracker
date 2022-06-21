var threads = [
  {
    id: 1,
    title: "Thread 1",
    author: "user1",
    date: Date.now(),
    content: "Thread content",
    comments: [
      {
        author: "Aaditya",
        date: Date.now(),
        content: "hey there",
      },
      {
        author: "Rathi",
        date: Date.now(),
        content: "wass up?",
      },
    ],
  },
  {
    id: 2,
    title: "Thread 2",
    author: "user2",
    date: Date.now(),
    content: "Thread content 2",
    comments: [
      {
        author: "Aaditya",
        date: Date.now(),
        content: "hey there",
      },
      {
        author: "Rathi",
        date: Date.now(),
        content: "wass up?",
      },
    ],
  },
];

var threads = defaultThreads;
if (localStorage && localStorage.getItem("threads")) {
  threads = JSON.parse(localStorage.getItem("threads"));
} else {
  threads = defaultThreads;
  localStorage.setItem("threads", JSON.stringify(defaultThreads));
}
