export default function Home() {
  return (
    <div className="flex items-center justify-center h-[calc(100vh-80px)] px-4">
      <div className="text-center">
        <h2
          className="text-3xl font-semibold mb-4"
          style={{ color: "#003145" }}
        >
          Welcome to aiPlanet pdf q&a
        </h2>
        <p className="text-lg" style={{ color: "#003145" }}>
          Upload a PDF and ask questions about its content.
        </p>
      </div>
    </div>
  );
}
