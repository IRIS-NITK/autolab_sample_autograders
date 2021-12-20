require "AssessmentBase.rb"

module MaxList
  include AssessmentBase

  def assessmentInitialize(course)
    super("max_list",course)
    @problems = []
  end

end
