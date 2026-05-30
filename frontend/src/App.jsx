import { useState } from "react"
export default function App() {
  const [journal, setJournal] = useState("")
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [ratings, setRatings] = useState({})
  const [hovered, setHovered] = useState({})

  const handleSubmit = async () => {
    if (!journal.trim() || journal.trim().length < 10) {
      setError("Please write at least a sentence about how you're feeling.")
    return
    }
    
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: journal })
      })

      if (!response.ok) throw new Error("Something went wrong")
      
      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError("Failed to get recommendations. Make sure the backend is running.")
    } finally {
      setLoading(false)
    }
  }

  const handleRating = (movieTitle, rating) => {
    setRatings(prev => ({
      ...prev,
      [movieTitle]: prev[movieTitle] === rating ? 0 : rating
    }))
  }

  return (
    <div className="min-h-screen bg-gray-950 text-white p-8">
      <div className="max-w-3xl mx-auto">
        
        {/* Header */}
        <div className="mb-10 text-center">
          <h1 className="text-4xl font-bold mb-2">🎬CineFeels</h1>
          <p className="text-gray-400">Write how you feel. We'll find the perfect film.</p>
        </div>

        {/* Journal Input */}
        <div className="mb-6">
          <textarea
            className="w-full h-40 bg-gray-900 border border-gray-700 rounded-xl p-4 text-white placeholder-gray-500 focus:outline-none focus:border-blue-500 resize-none"
            placeholder="Write about how you're feeling today..."
            value={journal}
            onChange={(e) => {
              setJournal(e.target.value)
              setError(null)
            }}
          />
          <p className="text-gray-500 text-xs mt-1 text-right">
            {journal.length} characters {journal.length < 10 && journal.length > 0 ? "— write a bit more!" : ""}
          </p>
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="mt-3 w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 text-white font-semibold py-3 rounded-xl transition"
          >
            {loading ? "Finding your films..." : "Find My Films"}
          </button>
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-900 border border-red-700 text-red-200 p-4 rounded-xl mb-6">
            {error}
          </div>
        )}

        {/* Results */}
        {result && (
          <div>
            {/* Emotion detected */}
            <div className="mb-6 bg-gray-900 border border-gray-700 rounded-xl p-4">
              <p className="text-gray-400 text-sm">Detected emotion</p>
              <p className="text-2xl font-bold capitalize">{result.emotion} <span className="text-gray-400 text-sm font-normal">({Math.round(result.confidence * 100)}% confidence)</span></p>
              <div className="flex flex-wrap gap-2 mt-2">
                {result.themes.map(theme => (
                  <span key={theme} className="bg-gray-800 text-gray-300 text-xs px-3 py-1 rounded-full">
                    {theme}
                  </span>
                ))}
              </div>
            </div>

            {/* Movie recommendations */}
            <div className="space-y-4">
              {result.recommendations.map((movie, index) => (
                <div key={index} className="bg-gray-900 border border-gray-700 rounded-xl p-5 flex gap-5">
                  {/* Poster */}
                  <img
                    src={`https://image.tmdb.org/t/p/w200${movie.poster_path}`}
                    alt={movie.title}
                    className="w-24 h-36 object-cover rounded-lg flex-shrink-0"
                  />
                  {/* Info */}
                  <div className="flex flex-col justify-between">
                    <div>
                      <h2 className="text-xl font-bold">{movie.title}</h2>
                      <p className="text-gray-400 text-sm mt-1">⭐ {movie.vote_average.toFixed(1)}</p>
                      <p className="text-gray-300 text-sm mt-2 line-clamp-2">{movie.overview}</p>
                    </div>
                    <p className="text-blue-400 text-sm mt-3 italic">{movie.explanation}</p>
                    {/* Star Rating */}
                    <div className="flex gap-1 mt-2">
                    {[1, 2, 3, 4, 5].map(star => (
                      <button
                        key={star}
                        onClick={() => handleRating(movie.title, star)}
                        onMouseEnter={() => setHovered(prev => ({ ...prev, [movie.title]: star }))}
                        onMouseLeave={() => setHovered(prev => ({ ...prev, [movie.title]: 0 }))}
                        className={`text-xl transition ${
                          (hovered[movie.title] || ratings[movie.title]) >= star
                            ? "text-yellow-400"
                            : "text-gray-600"
                        } hover:scale-110`}
                      >
                        ★
                      </button>
                    ))}
                  </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  )
}