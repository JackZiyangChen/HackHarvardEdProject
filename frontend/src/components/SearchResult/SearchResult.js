import React from 'react';
import data from './College_Data_Dict.json'
import './SearchResult.css';

const SearchResult = (props) => {
  const filteredData = data.filter((el) => {
    if (props.input === '') {
      return el;
    } else {
      return el.name.toLowerCase().startsWith(props.input)
    }
  })
  return (
    <>
      {props.input ? 
      <ul className="SearchResult">
        {filteredData.map((data) => (
          <li key={data.id} className="SearchResult-Cell">{data.name}</li>
        ))}
      </ul> : null }
    </>
  )
}

export default SearchResult;