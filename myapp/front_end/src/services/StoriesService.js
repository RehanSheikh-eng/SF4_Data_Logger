// StoriesService.js
import { useState, useEffect } from 'react';
import firebase from './firebase';

const useStoriesService = () => {
  const [stories, setStories] = useState([]);

  useEffect(() => {
    const unsubscribe = firebase.firestore().collection('stories')
      .onSnapshot(snapshot => {
        const newStories = snapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));

        setStories(newStories);
      });

    // Clean up the subscription on unmount
    return () => unsubscribe();
  }, []);

  return stories;
};

export default useStoriesService;
