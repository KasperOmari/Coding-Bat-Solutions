def cigar_party(cigars, is_weekend):
  return (cigars in range(40,61)) if not is_weekend else (cigars >= 40)

