import React from 'react';

const Post = ({ id, username, text, liked, onLike, onDelete, tag, onTagClick, selectedTags }) => {
  const isSelected = selectedTags.includes(tag);

  return (
    <div className="post-container">
      <p onClick={() => onTagClick(tag)} className={`post-username ${isSelected ? 'bold' : 'normal'}`}>
        {`${username} #${tag}`}
      </p>
      <p className="post-text">{text}</p>
      <p onClick={onLike} className="post-like" style={{ color: liked ? 'red' : 'black' }}>
        {liked ? 'Liked!' : 'Like post'}
      </p>
      <p onClick={() => onDelete(id)} className="post-delete" style={{ color: 'blue' }}>
        Удалить пост
      </p>
    </div>
  );
};

export default Post;
