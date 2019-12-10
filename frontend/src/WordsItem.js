import React from "react";

const WordsItem = ({ text, id, handleClick}) => {
    return (
        <div>
            <p>{words}</p>
            <button onClick={ () => handleClick(id) }> 삭제 </button>
        </div>
    );
    
};

export default WordsItem;