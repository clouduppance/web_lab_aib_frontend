import React, { useState} from 'react';
import Post from './Post';
import './PostList.css';

const PostList = () => {
  const [posts, setPosts] = useState([]);
  const [newPost, setNewPost] = useState({ username: '', text: '', tag: '' });
  const [selectedTags, setSelectedTags] = useState([]);
  const [tags, setTags] = useState([]);

  const handleLike = (postId) => {
    setPosts((prevPosts) =>
      prevPosts.map((post) =>
        post.id === postId ? { ...post, liked: !post.liked } : post
      )
    );
  };

  const handleDelete = (postId) => {
    setPosts((prevPosts) => prevPosts.filter((post) => post.id !== postId));
  };

  const handleAddPost = () => {
    const addedPost = {
      id: posts.length + 1,
      username: newPost.username,
      tag: newPost.tag,
      text: newPost.text,
      liked: false,
    };

    setPosts((prevPosts) => [...prevPosts, addedPost]);
    setNewPost({ username: '', text: '', tag: '' });
    setTags((prevTags) => Array.from(new Set([...prevTags, addedPost.tag])));
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewPost((prevNewPost) => ({ ...prevNewPost, [name]: value }));
  };

  const handleTagClick = (tag) => {
    setSelectedTags((prevTags) =>
      prevTags.includes(tag) ? prevTags.filter((t) => t !== tag) : [...prevTags, tag]
    );
  };

  const handleTagFilter = (tag) => {
    setSelectedTags((prevTags) =>
      prevTags.includes(tag) ? prevTags.filter((t) => t !== tag) : [...prevTags, tag]
    );
  };

  const filteredPosts = selectedTags.length
    ? posts.filter((post) => selectedTags.includes(post.tag))
    : posts;

  return (
    <div className="post-list-container">
      <h1>Список постов</h1>
      <div className='post-add'>
        <label>
          Имя пользователя:
          <input type="text" name="username" value={newPost.username} onChange={handleInputChange} />
        </label>
        <label>
          Текст поста:
          <input type="text" name="text" value={newPost.text} onChange={handleInputChange} />
        </label>
        <label>
          Тег:
          <input type="text" name="tag" value={newPost.tag} onChange={handleInputChange} />
        </label>
        <button onClick={handleAddPost}>Добавить пост</button>
      </div>
      <h1>Посты:</h1>
      <div>
        <p>Фильтр по тэгам:</p>
        {tags.map((tag) => (
          <span key={tag} onClick={() => handleTagFilter(tag)} style={{ cursor: 'pointer', marginLeft: '5px', fontWeight: selectedTags.includes(tag) ? 'bold' : 'normal' }}>#{tag}</span>))}
      </div>
      {filteredPosts.map((post) => (
        <Post
          key={post.id}
          id={post.id}
          username={post.username}
          text={post.text}
          tag={post.tag}
          liked={post.liked}
          onLike={() => handleLike(post.id)}
          onDelete={handleDelete}
          onTagClick={handleTagClick}
          selectedTags={selectedTags}
        />
      ))}
    </div>
  );
};

export default PostList;