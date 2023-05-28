import { useState, useEffect } from 'react';
import { collection, onSnapshot } from 'firebase/firestore';
import db from './firebase';

const useStoriesService = () => {
  const [stories, setStories] = useState([]);

  useEffect(() => {
    const storiesCollection = collection(db, 'stories');

    const unsubscribe = onSnapshot(storiesCollection, (snapshot) => {
      const newStories = snapshot.docs.map((doc) => ({
        id: doc.id,
        ...doc.data(),
      }));

      setStories(newStories);
    });

    // Clean up the subscription on unmount
    return () => unsubscribe();
  }, []);

  return stories;
};

export default useStoriesService;
